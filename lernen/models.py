from django.db import models
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField


class Kapitel(models.Model):
    kapitelname = models.CharField(max_length=30)

    def __str__(self):
        return self.kapitelname


class Artikel(models.Model):
    title = models.CharField(max_length=100)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    unterschrift = models.CharField(max_length=100, blank=True,  null=True)
    kapitel = models.ForeignKey(Kapitel)
    text = models.TextField()
    unten = models.BooleanField(default=False)  # um fragen ob Bilder unten angezeigt werden sollen
    video = models.URLField(max_length=200, blank=True)
    content = RichTextField(blank=True,  null=True)

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return self.title


class ArtikelImages(models.Model):
    article = models.ForeignKey(Artikel)
    imgname = models.CharField(max_length=30)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    image = models.ImageField(blank=False, null=False, upload_to="article/")

    class Meta(object):
        ordering = ['order']
