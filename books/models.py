from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, blank=False, null=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=200)
    isbn13 = models.CharField(max_length=13)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    publisher = models.CharField(max_length=50)
    pages = models.IntegerField()
    year_published = models.IntegerField()

    def __str__(self):
        return self.title