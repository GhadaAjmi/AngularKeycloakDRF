import logging

from django.contrib.auth.models import AnonymousUser
from keycloak import KeycloakOpenID
from keycloak import KeycloakError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

KEYCLOAK_OPENID = KeycloakOpenID(
    server_url="http://localhost:8080",
    client_id="keycloak-django",
    realm_name="keycloak-angular-sandbox",
    client_secret_key="GP6omOX1JlpmLLU01blA5IrgE2JRh6fh" 
)

logger = logging.getLogger(__name__)

class TokenNoopUser(AnonymousUser):
    """
    Django Rest Framework needs an user to consider authenticated
    """

    def __init__(self, user_info):
        super().__init__()
        self.user_info = user_info

    @property
    def is_authenticated(self):
        return True

class KeyCloakAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization")
        if not token:
            raise AuthenticationFailed()

        try:
            token = token.split(' ')[1]

            # _, token = token.split(" ")
            logger.info(token)
            user_info = KEYCLOAK_OPENID.userinfo(token)
        except (AttributeError, KeycloakError):
            raise AuthenticationFailed()
        return (TokenNoopUser(user_info=user_info), None)
