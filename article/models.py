import random
import string

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


def rand_slug():
    # return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    return ''.join(random.choice(string.ascii_letters + string.digits))


class Categories(models.Model):
    sts = (
        ('green', 'green'),
        ('blue', 'blue'),
        ('cyan', 'cyan'),
        ('orange', 'orange'),
        ('purple', 'purple'),
        ('red', 'red'),
        ('violet', 'violet'),
    )
    name = models.CharField(max_length=30)
    color = models.CharField(choices=sts, default='blue', max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kategoriya"


class Regions(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Viloyat"


class Article(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='article')
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    views = models.PositiveIntegerField(default=0)
    # is_top = models.BooleanField(default=False)
    ips = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Maqola"

    def views_count(self):
        self.views += 1
        self.save()

    def get_absolute_url(self):
        return reverse('manage', )

    # def save(self, *args, **kwargs):  # new
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class AboutUs(models.Model):
    text = RichTextField()

    class Meta:
        verbose_name_plural = "Biz Haqimizda"


class Advertisement(models.Model):
    company = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to='advertisement')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = "reklama"
