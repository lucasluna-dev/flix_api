from rest_framework import serializers
from movies.models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'
        
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1990.")
        return value
    
    def validate_resume(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("O resumo não pode ter mais de 100 caracteres.")
        return value