import json

from oauth2_provider.views import TokenView
from oauth2_provider.models import AccessToken
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters


@method_decorator(sensitive_post_parameters("password"))
class CustomAuthResponse(TokenView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            data = response.content.decode('utf-8')
            data_dict = json.loads(data)
            access_token = AccessToken.objects.get(token=data_dict['access_token'])
            user = access_token.user
            data_dict['user'] = {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
            body = json.dumps(data_dict)
            return HttpResponse(content=body, status=response.status_code, )
        else:
            return response
