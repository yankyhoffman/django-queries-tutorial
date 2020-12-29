from datetime import datetime

from django.core.management import BaseCommand

from books.models import Author, Book


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Book.objects.all().delete()
        Author.objects.all().delete()

        for name, books in [
            ('Alice', [
                ('The Great Read', datetime(2020, 11, 1)),
                ('Super Duper Book', datetime(2020, 12, 15)),
            ]),
            ('Bob', [
                ('Mystery Novel', datetime(2020, 10, 1)),
                ('Hidden Secrets', datetime(2020, 11, 10)),
                ('The Great Reveal', datetime(2020, 11, 20)),
            ]),
            ('Charlie', [
                ('Secrets of the Place', datetime(2021, 2, 15)),
                ('Survival Guide', datetime(2020, 12, 15)),
            ]),
        ]:
            author = Author(name=name)
            author.save()

            for book in books:
                Book(
                    title=book[0],
                    published=book[1],
                    author=author,
                ).save()
