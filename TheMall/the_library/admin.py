from django.contrib import admin
from .models import Librarian, Desk, Author, Book, Reader

# 🧑‍💼 Basic model registrations:
@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # columns shown in admin list
    search_fields = ('name',)


@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'librarian')
    list_filter = ('number',)
    search_fields = ('librarian__name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'author__name')


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    filter_horizontal = ('books',)  # nice widget for many-to-many
    search_fields = ('name',)
