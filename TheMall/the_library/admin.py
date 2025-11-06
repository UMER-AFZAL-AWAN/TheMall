from django.contrib import admin
from .models import Librarian, Desk, Author, Book, Reader, Student, Enrollment, StudentProfile

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


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_no')
    search_fields = ('name', 'roll_no')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course_name', 'semester')
    list_filter = ('course_name', 'semester')
    search_fields = ('student__name',)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'gpa', 'attendance_percentage')
    search_fields = ('enrollment__student__name',)