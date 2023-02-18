from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час редагування')
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')
    # from_username = models.CharField(max_length=255, db_index=True, verbose_name='Користувач')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Каталог')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        ordering = ['-id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Name")
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорія'
        ordering = ['id']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile', verbose_name='Користувач')
    username = models.CharField(max_length=255, unique=True, db_index=True, null=True, verbose_name='Логін')
    bio = models.TextField(blank=True, verbose_name='Біографія')
    photo = models.ImageField(upload_to='profile/', blank=True, null=True, verbose_name='Фото')


    # def get_absolute_url(self):
    #     return reverse('profile', kwargs={'username': self.user.username})

    def get_absolute_url(self):
        # if self.username:
        #     username = Profile.objects.get(username__iexact=self.username).username
        #     print(username)
        
        return reverse('profile', kwargs={'username': self.username})


    def __str__(self):
        return str(self.user)


    class Meta:
        verbose_name = 'Профілі'
        verbose_name_plural = 'Профіль'
        ordering = ['-pk']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(instance)
        Profile.objects.create(user=instance, username=instance.username)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()