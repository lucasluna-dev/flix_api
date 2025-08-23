from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermissionClass
from movies.models import Movies
from movies.serializers import MoviesSerializer

class MoviesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissionClass,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer 
    

class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissionClass,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    
    
