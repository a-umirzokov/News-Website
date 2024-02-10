from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='PU')


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-id']

    def __str__(self):
        return self.name


class News(models.Model):

    class Status(models.TextChoices):
        Published = 'PU', 'Published'
        Draft = 'DR', 'Draft'

    title = models.CharField(max_length=150, verbose_name='Title')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    body = models.TextField(verbose_name='Text')
    image = models.ImageField(upload_to='static/images', verbose_name='Image')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category')
    published_time = models.DateTimeField(default=timezone.now, verbose_name='Published time')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Created time')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Updated time')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft, verbose_name='Status')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-published_time']
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(max_length=100, verbose_name='Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Phone')
    subject = models.CharField(max_length=100, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Created time')

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.email