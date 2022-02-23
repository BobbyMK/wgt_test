from django.db import models
from django.contrib.auth.models import User


RATING_CHOICE = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]

class Survey(models.Model):

    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, db_index=True)
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICE,
        verbose_name='Рейтинг',
        db_index=True
    )
    review = models.CharField(max_length=300, verbose_name='Текст', blank=True, db_index=True)
    created = models.DateTimeField(verbose_name="Время создания", auto_now_add=True, db_index=True)
    published = models.BooleanField(default=False, verbose_name='Опубликован', db_index=True)

    def __str__(self):
        return f'{self.author}: {self.review}'


    def publish(self):
        self.published = True
        self.save()

    def send_request(self):
        """
        Отправляем запрос с данными в формате JSON
        """
        import requests

        url = 'https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4'
        data = {
            'author': self.author.id,
            'rating': self.rating,
            'review': self.review
            }
        r = requests.post(url, json=data)

    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'