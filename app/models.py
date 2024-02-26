from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_image(self):
        return self.image
    
    def get_created_at(self):
        return self.created_at
    
    