from django.core.management.base import BaseCommand
from articles.models import Tag


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        tag_list = [
            'Здоровье',
            'Город',
            'Культура',
            'Наука',
            'Космос',
            'Международные отношения',
            'Спорт',
            'Политика',
            'Животные',
            'Экономика',
            'Происшествия',
            'Авто',
            'Коронавирус'
        ]

        for tag in tag_list:
            tags = Tag(name=tag)
            tags.save()
