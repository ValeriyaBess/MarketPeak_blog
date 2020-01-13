from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Post(models.Model):
    url_name = models.CharField(max_length=1000, verbose_name='URL страницы', unique=True)
    title = models.CharField(max_length=1000, verbose_name='Название поста', unique=True, default="")
    title_description = models.CharField(max_length=1000, verbose_name='Краткое описание поста', null=True, blank=True)
    image = models.ImageField('Фото поста', null=True, blank=True)
    text = RichTextUploadingField(verbose_name="Текст поста")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    hidden_post = models.BooleanField(default=False)
    count_block_in_line = models.IntegerField(default=3)
    date_creation = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата и время последнего изменения', auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title} ({self.category})'

    def col(self):
        return int(12 / self.count_block_in_line)


class Comment(models.Model):
    message = models.TextField(verbose_name="Сообщение")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    date_creation = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата и время последнего изменения', auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.message} ({self.user}). Пост: {self.post}'
