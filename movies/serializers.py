from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movies
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer

class MoviesSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = Movies
        fields = '__all__'
        
        
    def validate_release_date(self, value):
        if value is not None and value.year < 1990:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1990.")
        return value
    
    def validate_resume(self, value):
        if value is not None and len(value) > 100:
            raise serializers.ValidationError("O resumo não pode ter mais de 100 caracteres.")
        return value
    
class MovieListDetailSerializer(serializers.ModelSerializer):# aplicando o conceito de backend for frontend (BFF)
    
    class Meta:
        model = Movies
        fields = '__all__'
    actors = ActorSerializer(many=True, read_only=True)
    genre = GenreSerializer(read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)
    #  media de avaliações por filme
    def get_rate(self, obj):
        avg = obj.reviews.aggregate(avg=Avg('stars'))['avg']
        return avg or 0
    
   