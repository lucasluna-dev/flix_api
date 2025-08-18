from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movies

class Review(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, 'avaliação deve ser maior ou igual a 1'),
            MaxValueValidator(5, 'avaliação deve ser menor ou igual a 5')
        ]
    )  
    comment = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'Review for {self.movie.title} - {self.stars} stars'

    
