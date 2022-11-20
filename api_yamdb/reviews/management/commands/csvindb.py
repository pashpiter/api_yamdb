from django.core.management.base import BaseCommand
from django.conf import settings

import csv

from reviews.models import (Category, Comment, GenreTitle, 
                            Genre, Review, Title, User)


CSV_FILES = {
    User: 'users.csv',
    Category : 'category.csv',
    Comment : 'comments.csv',
    GenreTitle : 'genre_title.csv',
    Genre : 'genre.csv',
    Review : 'review.csv',
    Title : 'titles.csv'
}

class Command(BaseCommand):

    def handle(self, *args, **options):
        for model, file in CSV_FILES.items():
            with open(
                f'{settings.BASE_DIR}/static/data/{file}',
                encoding='utf-8'
                ) as csvfile:
                for row in csv.DictReader(csvfile):
                    model.objects.create(**dict(row))