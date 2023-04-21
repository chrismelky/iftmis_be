from rest_framework import viewsets
from rest_framework.response import Response

def custom_response(data, **kwargs):
    return Response(data={'data': data, **kwargs})


class BaseViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'

    def list(self, request, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return custom_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return custom_response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user.username)
        return custom_response(serializer.data, message='Successfully created')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=request.user.email)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return custom_response(serializer.data, message='Successfully update')

    def destroy(self, request, *args, **kwargs):
        self.lookup_field = 'parent_id'
        instance = self.get_object()
        self.perform_destroy(instance)
        return custom_response(data=None, message='Successfully deleted')