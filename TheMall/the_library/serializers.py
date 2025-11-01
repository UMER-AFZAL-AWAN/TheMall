from rest_framework import serializers
from .models import Librarian, Desk, Author, Book, Reader


# 1️⃣ Librarian Serializer
class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'


# 2️⃣ Desk Serializer (One-to-One)
class DeskSerializer(serializers.ModelSerializer):
    librarian = LibrarianSerializer(read_only=True)
    librarian_id = serializers.PrimaryKeyRelatedField(
        queryset=Librarian.objects.all(), source='librarian', write_only=True
    )

    class Meta:
        model = Desk
        fields = ['id', 'number', 'librarian', 'librarian_id']


# 3️⃣ Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


# 4️⃣ Book Serializer (One-to-Many → Author to Books)
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id']


# 5️⃣ Reader Serializer (Many-to-Many with Books)
class ReaderSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True)
    book_ids = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), many=True, source='books', write_only=True
    )

    class Meta:
        model = Reader
        fields = ['id', 'name', 'books', 'book_ids']
