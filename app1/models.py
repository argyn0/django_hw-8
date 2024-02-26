from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'MyModel'
        verbose_name_plural = 'MyModels'

    def __str__(self):
        return self.name