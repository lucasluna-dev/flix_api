from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
   
    class Meta:
        model = Movies
        fields = '__all__'
        
     # somar todas as avaliações de um filme (media)
    def get_rate(self, obj):
        avg = obj.reviews.aggregate(avg=Avg('stars'))['avg']
        return avg or 0
        
    def validate_release_date(self, value):
        if value is not None and value.year < 1990:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1990.")
        return value
    
    def validate_resume(self, value):
        if value is not None and len(value) > 100:
            raise serializers.ValidationError("O resumo não pode ter mais de 100 caracteres.")
        return value
