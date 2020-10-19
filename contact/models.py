from django.db import models

# Create your models here.

class Info(models.Model):
    place        = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email        = models.EmailField(max_length=100)

    class Meta:
        verbose_name=('Info')
        verbose_name_plural=("Information")


    def __str__(self):
        return self.email