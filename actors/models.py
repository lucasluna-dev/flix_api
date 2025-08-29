from django.db import models


NATIONALITY_CHOICES = [
    ('USA', 'Estados Unidos'),
    ('MEXICAN', 'Mexican'),
    ('FRENCH', 'French'),
    ('BRAZIL', 'Brazilian'),
    ('ITALIAN', 'Italian'),
    ('GERMAN', 'German'),
    ('BRITISH', 'British'),
    ('CANADIAN', 'Canadian'),
    ('AUSTRALIAN', 'Australian'),
    ('OTHER', 'Other'), 
]

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.name
