from django.db import models

# Create your models here.

class Income(models.Model):
    model = models.CharField(max_length=255, verbose_name='Modeli')
    name = models.CharField(max_length=255, verbose_name='Nomi')




    def __str__(self):
        return self.name




    class Meta:
        verbose_name = 'Noutbook'
        verbose_name_plural = 'Noutbooklar'
