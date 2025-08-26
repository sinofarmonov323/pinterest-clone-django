from django.db import models
import os

# Create your models here.

class PostImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        print(self.image.path)
        os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def change(self, *args, **kwargs):
        os.remove(self.image.path)
        super().change(*args, **kwargs)
