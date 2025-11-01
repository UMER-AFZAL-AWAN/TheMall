from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LibrarianViewSet,
    DeskViewSet,
    AuthorViewSet,
    BookViewSet,
    ReaderViewSet
)

router = DefaultRouter()
router.register(r'librarians', LibrarianViewSet)
router.register(r'desks', DeskViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'readers', ReaderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
