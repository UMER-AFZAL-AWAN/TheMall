from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
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

    # # 🧩 Custom endpoint to get a librarian and their desk
    # @action(detail=True, methods=['get'])
    # def with_desk(self, request, pk=None):

    #     """
    #     GET /librarians/{id}/with_desk/
    #     Returns librarian details along with their assigned desk.
    #     """

    #     librarian = self.get_object()
    #     desk = getattr(librarian, 'desk', None)  # handle if desk doesn’t exist

    #     librarian_data = LibrarianSerializer(librarian).data
    #     desk_data = DeskSerializer(desk).data if desk else None

    #     return Response({
    #         "librarian": librarian_data,
    #         "desk": desk_data
    #     })



    # 🧩 Custom endpoint to get librarian and desk in a single query
    @action(detail=True, methods=['get'])
    def with_desk(self, request, pk=None):
        """
        GET /librarians/{id}/with_desk/
        Returns librarian details along with their assigned desk,
        using select_related() to avoid multiple DB queries.
        """
        # ✅ Fetch librarian + related desk in one query
        librarian = Librarian.objects.select_related('desk').get(pk=pk)

        # Accessing related desk doesn’t hit the DB again
        desk = getattr(librarian, 'desk', None)

        librarian_data = LibrarianSerializer(librarian).data
        desk_data = DeskSerializer(desk).data if desk else None

        return Response({
            "librarian": librarian_data,
            "desk": desk_data
        })


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
