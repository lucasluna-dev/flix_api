from django.contrib.auth import get_user_model  # obtém o model de usuário ativo
from django.contrib.auth.models import Group  # grupos e permissões do Django
from rest_framework import generics, permissions, response, status  # views genéricas e permissões do DRF

from .serializers import RegisterSerializer, UserSerializer  # serializers de cadastro e de saída do usuário


User = get_user_model()  # resolve dinamicamente o User (padrão ou custom)


class RegisterView(generics.CreateAPIView):  # endpoint de cadastro (POST)
    permission_classes = (permissions.AllowAny,)  # permite acesso sem autenticação
    serializer_class = RegisterSerializer  # valida e cria usuário com senha hasheada

    def perform_create(self, serializer):  # hook chamado após validação para salvar e aplicar regras extras
        user = serializer.save()  # cria o usuário usando o serializer (usa set_password internamente)
        # Adiciona o usuário ao grupo padrão, se existir
        try:
            default_group = Group.objects.get(name="default_viewer")  # grupo com permissões view_*
            user.groups.add(default_group)  # concede permissões de leitura conforme GlobalDefaultPermissionClass
        except Group.DoesNotExist:
            # Grupo ainda não criado; segue sem bloquear o cadastro
            pass
        return user


class MeView(generics.RetrieveAPIView):  # endpoint para obter dados do usuário autenticado
    permission_classes = (permissions.IsAuthenticated,)  # exige JWT válido
    serializer_class = UserSerializer  # controla os campos expostos

    def get_object(self):  # retorna o próprio usuário do request
        return self.request.user
