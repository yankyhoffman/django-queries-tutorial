from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=200)
    published = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
