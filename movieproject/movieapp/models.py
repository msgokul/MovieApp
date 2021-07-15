from django.db import models

# create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.name