from django.urls import path
from . import views


urlpatterns = [
    
    path('movies/', views.MoviesCreateListView.as_view(), name='movies-create-list'),  
    path('movies/<int:pk>/', views.MoviesRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
    
]