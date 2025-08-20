from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView,TokenVerifyView # Importa a view para gerar o token JWT, já possui a lógica de autenticação pegando dados do usuario no BD

urlpatterns = [
    
   path('authentication/token/', TokenObtainPairView.as_view() , name='token_obtain_pair'), # url para gerar json web token
   path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]