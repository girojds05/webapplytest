from django.db import models

# Create your models here.
# class SampleModel(models.Model):
#     title=models.CharField(max_length=100)
#     number=models.IntegerField()
#     # content=models.TextField()
#     # def __str__(self):
#     #     return self.title

CATEGORY = (('business','ビジネス'), ('life','生活'), ('other','その他'))

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(choices=CATEGORY, max_length=100)
    # memo = models.TextField()
    def __str__(self):
        return self.title