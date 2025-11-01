from rest_framework import viewsets
from .models import Librarian, Desk, Author, Book, Reader
from .serializers import (
    LibrarianSerializer,
    DeskSerializer,
    AuthorSerializer,
    BookSerializer,
    ReaderSerializer
)


# 1️⃣ Librarian CRUD
class LibrarianViewSet(viewsets.ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer


# 2️⃣ Desk CRUD
class DeskViewSet(viewsets.ModelViewSet):
    queryset = Desk.objects.all()
    serializer_class = DeskSerializer


# 3️⃣ Author CRUD
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# 4️⃣ Book CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# 5️⃣ Reader CRUD
class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
