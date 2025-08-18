from django.contrib import admin
from movies.models import Movies


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'release_date', 'genre','resume')
    search_fields = ('title','genre')
    list_filter = ('genre', 'release_date',)
