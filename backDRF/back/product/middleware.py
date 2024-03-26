# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.authentication import BaseAuthentication
# from jwt import decode as decode_jwt, InvalidTokenError

# class TokenValidationMiddleware(BaseAuthentication):
#     def authenticate(self, request):
#         authorization_header = request.headers.get('Authorization')

#         if authorization_header is None:
#             return None  # Aucun jeton trouvé dans l'en-tête

#         parts = authorization_header.split()
#         if len(parts) != 2 or parts[0].lower() != 'bearer':
#             return None  # L'en-tête n'est pas correctement formaté

#         token = parts[1]
#         # Validation du jeton avec la bibliothèque JWT (non exhaustif, assurez-vous de configurer correctement votre validation)
#         try:
#             decoded_token = decode_jwt(token, verify=False)  # Vous devez configurer la vérification selon votre configuration
#             # Vous pouvez effectuer d'autres vérifications des revendications du jeton ici si nécessaire

#             # Si le jeton est valide, vous pouvez retourner une paire (utilisateur, jeton)
#             return (decoded_token['user'], token)
#         except InvalidTokenError:
#             return None  # Jeton invalide

#     def authenticate_header(self, request):
#         return 'Bearer'  # Indique au client que l'authentification est requise avec un jeton Bearer
