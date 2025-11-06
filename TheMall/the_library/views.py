from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Librarian, Desk, Author, Book, Reader,  Student, Enrollment, StudentProfile
from .serializers import (
    LibrarianSerializer,
    DeskSerializer,
    AuthorSerializer,
    BookSerializer,
    ReaderSerializer,
    AuthorWithBooksSerializer,
    StudentSerializer, 
    EnrollmentSerializer, 
    StudentProfileSerializer
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

    # 🆕 Create author + multiple books in one API
    @action(detail=False, methods=['post'])
    def create_with_books(self, request):
        serializer = AuthorWithBooksSerializer(data=request.data)
        if serializer.is_valid():
            author = serializer.save()
            return Response(AuthorSerializer(author).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #!     POST /api/library/authors/create_with_books/



# 4️⃣ Book CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # 🆕 Get all readers who borrowed this book
    @action(detail=True, methods=['get'])
    def borrowed_by(self, request, pk=None):
        book = self.get_object()
        readers = book.reader_set.all()  # reverse relation
        data = ReaderSerializer(readers, many=True).data
        return Response({
            "book": book.title,
            "borrowed_by": data
        })


# 5️⃣ Reader CRUD
class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

    # 🆕 Get all books borrowed by this reader
    @action(detail=True, methods=['get'])
    def borrowed_books(self, request, pk=None):
        reader = self.get_object()
        books = reader.books.all()
        data = BookSerializer(books, many=True).data
        return Response({
            "reader": reader.name,
            "borrowed_books": data
        })


# 6️⃣ Student CRUD
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# 7️⃣ Enrollment CRUD
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.select_related('student').all()
    serializer_class = EnrollmentSerializer


# 8️⃣ StudentProfile CRUD (Main interaction point)
class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.select_related('enrollment__student').all()
    serializer_class = StudentProfileSerializer

    # 🆕 Example custom action: fetch full chain (Profile → Enrollment → Student)
    @action(detail=True, methods=['get'])
    def full_details(self, request, pk=None):
        profile = self.get_object()
        data = {
            "profile": StudentProfileSerializer(profile).data,
            "enrollment": EnrollmentSerializer(profile.enrollment).data,
            "student": StudentSerializer(profile.enrollment.student).data
        }
        return Response(data)