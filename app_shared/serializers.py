from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(allow_null=True, read_only=True)
    created_by = serializers.CharField(max_length=100, read_only=True)
    updated_by = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        extra_kwargs = {'created_by': {'read_only': True}, 'updated_by': {'read_only': True}}
