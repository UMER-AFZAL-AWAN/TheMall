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


