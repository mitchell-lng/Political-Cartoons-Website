from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.


class Cartoon(models.Model):
    """Model to store political cartoons."""
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    final = models.ImageField(upload_to='cartoons')

    def __name__(self):
        return self.title + ' by ' + self.author
