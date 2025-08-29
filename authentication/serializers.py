from django.contrib.auth import get_user_model  # obtém o model de usuário ativo (custom ou padrão)
from rest_framework import serializers  # base para serializers do DRF


User = get_user_model()  # alias para o model de usuário


class UserSerializer(serializers.ModelSerializer):  # serializer de saída para expor dados do usuário
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")  # campos seguros (sem senha)
        read_only_fields = ("id",)  # id não pode ser alterado


class RegisterSerializer(serializers.ModelSerializer):  # serializer de entrada para cadastro
    password = serializers.CharField(write_only=True, min_length=8)  # não retorna no response
    password2 = serializers.CharField(write_only=True, min_length=8)  # confirmação de senha

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2", "first_name", "last_name")  # campos aceitos

    def validate(self, attrs):  # validação cruzada: confere se as senhas coincidem
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        return attrs

    def create(self, validated_data):  # criação do usuário com senha hasheada
        validated_data.pop("password2", None)  # remove campo auxiliar
        password = validated_data.pop("password")  # extrai a senha
        user = User(**validated_data)  # instancia sem senha
        user.set_password(password)  # aplica hash seguro
        user.save()
        return user
