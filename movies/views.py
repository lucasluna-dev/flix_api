from rest_framework import generics
from movies.models import Movies
from movies.serializers import MoviesSerializer

class MoviesCreateListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer 
    

class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    
    
