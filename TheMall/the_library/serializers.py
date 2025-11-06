from rest_framework import serializers
from .models import Librarian, Desk, Author, Book, Reader, Student, Enrollment, StudentProfile


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

# 🔹 New Serializer to Create Author + Books in One Request
class AuthorWithBooksSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, write_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        books_data = validated_data.pop('books', [])
        author = Author.objects.create(**validated_data)
        for book_data in books_data:
            Book.objects.create(author=author, **book_data)
        return author
    

# 6️⃣ Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# 7️⃣ Enrollment Serializer
class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student', write_only=True
    )

    class Meta:
        model = Enrollment
        fields = ['id', 'course_name', 'semester', 'student', 'student_id']


# 8️⃣ StudentProfile Serializer (connects to Enrollment)
class StudentProfileSerializer(serializers.ModelSerializer):
    enrollment = EnrollmentSerializer(read_only=True)
    enrollment_id = serializers.PrimaryKeyRelatedField(
        queryset=Enrollment.objects.all(), source='enrollment', write_only=True
    )

    class Meta:
        model = StudentProfile
        fields = ['enrollment_id', 'enrollment', 'gpa', 'attendance_percentage']
