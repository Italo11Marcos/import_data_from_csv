from django.contrib import admin
from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'isbn13', 'avg_rating', 'publisher', 'pages', 'year_published')
    search_fields = ('title', 'pages', 'year_published', 'author', 'publisher')

