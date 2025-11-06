# 📚 Super Simple Library Example
from django.db import models


# 1️⃣ One-to-One → each Librarian has exactly one Desk
class Librarian(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): 
        return self.name


class Desk(models.Model):
    librarian = models.OneToOneField(Librarian, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"Desk {self.number} ({self.librarian.name})"


# 2️⃣ One-to-Many → one Author can write many Books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# 3️⃣ Many-to-Many → a Reader can borrow many Books, and each Book can be borrowed by many Readers
class Reader(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='readers')

    def __str__(self):
        return self.name


# 4️⃣ Student → Enrollment → StudentProfile (Chained Relationship)

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.name} - {self.course_name}"


class StudentProfile(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE, primary_key=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    attendance_percentage = models.FloatField()

    def __str__(self):
        return f"Profile of {self.enrollment.student.name}"
