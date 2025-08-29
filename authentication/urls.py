from django.urls import path  # roteamento de URLs
from rest_framework_simplejwt.views import (
    TokenObtainPairView,   # endpoint de login: gera access/refresh
    TokenRefreshView,      # endpoint para renovar o access token
    TokenVerifyView,       # endpoint para verificar token
)
from .views import RegisterView, MeView  # views locais de cadastro e perfil

urlpatterns = [
    # JWT
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # verificação

    # Auth helpers
    path('authentication/register/', RegisterView.as_view(), name='auth_register'),  # cadastro
    path('authentication/me/', MeView.as_view(), name='auth_me'),  # perfil do usuário autenticado
]
