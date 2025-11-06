from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LibrarianViewSet,
    DeskViewSet,
    AuthorViewSet,
    BookViewSet,
    ReaderViewSet,
    StudentViewSet,
    EnrollmentViewSet,
    StudentProfileViewSet
)

router = DefaultRouter()
router.register(r'librarians', LibrarianViewSet)
router.register(r'desks', DeskViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'readers', ReaderViewSet)
router.register(r'students', StudentViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'student_profiles', StudentProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
