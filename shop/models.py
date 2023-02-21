from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns


class item(models.Model):
    ''' Регистрация модели товара '''
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID facross whole library")
    name  = models.CharField(max_length = 50, help_text = 'Название товара')
    description = models.CharField(max_length = 200, help_text = 'Описпние товара до 200 символов')
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text='цена')

    def get_absolute_url(self):
        print(f'\n  (self.id) : {str(self.id)} \n')
        return reverse('item_detail', args=[str(self.id)])

    
    def __str__(self): # выдача инфо о товаре
        
        return '%s, %s, %s' % (self.name, self.description, self.price)
    
    class Meta:
        ''' сортировка по имени  потом по цене'''
        ordering = ['name', 'price']
        
        

