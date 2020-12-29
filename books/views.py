from django.db.models import Prefetch, Window, F, RowRange
from django.db.models.functions import LastValue
from django.shortcuts import render

from .models import Author, Book


def index(request):
    newest_books = Book.objects.order_by('-published').first()

    authors = Author.objects.prefetch_related(
        Prefetch('book_set', queryset=newest_books, to_attr='newest_book')
    )

    return render(request, 'books/index.html', {'authors': authors})


def newest_books_by_author(request):
    """
    Try emulating the following query:
        select
            id,
            title,
            published,
            author_id,
            last_value(id) over (
                partition by author_id
                order by published
                range between unbounded preceding and unbounded following
            ) last
        from books_book
        order by author_id, published;
    """
    books = Book.objects.annotate(
        last_id=Window(
            expression=LastValue('id'),
            partition_by=F('author_id'),
            order_by=F('published'),
            frame=RowRange(start=None, end=None),
        )
    )

    return render(request, 'books/newest.html', {'books': books})
