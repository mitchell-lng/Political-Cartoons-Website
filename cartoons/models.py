from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.


class Cartoon(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    image = models.ImageField(upload_to='media/final/')

    @property
    def slug(self):
        return self.title.replace(" ", "-").lower()

    def __str__(self):
        return f'{self.title} by {self.author}'


class Draft(models.Model):
    cartoon = models.ForeignKey(Cartoon, on_delete=models.CASCADE)
    iteration = models.IntegerField()
    image = models.ImageField(upload_to='media/draft/')

    def __str__(self):
        return f'{self.cartoon.title} by {self.cartoon.author} draft {self.iteration}'
