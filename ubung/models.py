from django.db import models

class Bild(models.Model):
    title = models.CharField(max_length=30)
    image_name = models.CharField(max_length=30)
    auswahllocation = models.TextField()

    def __str__(self):
        return self.title

class UbungKapitel(models.Model):
    kapitelname = models.CharField(max_length=30)

    def __str__(self):
        return self.kapitelname

class Question(models.Model):
    uberschrift = models.CharField(max_length=40)
    text = models.TextField()
    frage = models.CharField(max_length = 300, null = True, blank = True)
    kapitel = models.ForeignKey(UbungKapitel)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    image = models.ImageField(blank = True, null = True, upload_to="ubung/")
    coordinates = models.TextField(blank = True)

    def __str__(self):
        return self.uberschrift

    class Meta(object):
        ordering = ['my_order']

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.TextField()
    richtig = models.BooleanField(default = True)
