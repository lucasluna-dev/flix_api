from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermissionClass 
from .models import Genre
from .serializers import GenreSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 