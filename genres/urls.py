from django.urls import path
from . import views

# versionamento de apis
urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre-create-list'),  
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),  


]