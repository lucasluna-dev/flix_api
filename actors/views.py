from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from actors.models import Actor
from  actors.serializers import ActorSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,IsAdminUser) PARA CASO APENAS OS USUÁRIOS ADMINISTRADORES PODEM CRIAR E LISTAR
    #permission_classes = (IsAuthenticatedOrReadOnly) PARA CASO APENAS OS USUÁRIOS AUTENTICADOS PODEM CRIAR, MAS TODOS PODEM LISTAR
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = 'id' # serve para especificar o campo usado para buscar o objeto
