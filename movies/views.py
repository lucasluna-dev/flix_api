from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg
from app.permission import GlobalDefaultPermissionClass
from movies.models import Movies
from movies.serializers import MoviesSerializer, MovieListDetailSerializer
from reviews.models import Review

class MoviesCreateListView(generics.ListCreateAPIView): 
    permission_classes = (IsAuthenticated,GlobalDefaultPermissionClass,)
    queryset = Movies.objects.all()
    #serializer_class = MoviesSerializer 
    
    # aplicando o conceito de backend for frontend (BFF)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MoviesSerializer
    

class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissionClass,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    
class MoviesStatsView(views.APIView): # nova view para estatísticas
    permission_classes = (IsAuthenticated,GlobalDefaultPermissionClass,)
    queryset = Movies.objects.all()
    
    def get(self, request):
        
        # Calcular estatisticas
        total_movies = self.queryset.count()
        total_movies_by_genre = self.queryset.values('genre__name').annotate(total_filmes=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        
        
        
        return response.Response(data={
            'total de filmes': total_movies,
            'total de filmes por genero': total_movies_by_genre,
            'total de reviews': total_reviews,
            'media de estrelas': round(average_stars, 1) if average_stars else 0,
        }, status=status.HTTP_200_OK)
       