from django.contrib import admin
from genres.models import Genre

@admin.register(Genre) # RServe para registrar o modelo Genre no admin
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
