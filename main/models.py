from django.db import models
import os

# Create your models here.

class PostImage(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    file = models.FileField(upload_to='uploads/', blank=False, null=False)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        print(f"Object: {self.file} - args: {args}, kwargs: {kwargs}")
        if self.file and os.path.isfile(self.file.path):
            os.remove(self.file.path)
        super().delete(*args, **kwargs)

    def change(self, *args, **kwargs):
        os.remove(self.file.path)
        super().change(*args, **kwargs)

    def is_image(self):
        return self.file.name.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        
    def is_video(self):
        return self.file.name.lower().endswith((".mp4", ".avi", ".mov", ".mkv"))

    def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
        if self.is_image() or self.is_video():
            super().save(force_insert, force_update, using, update_fields)
