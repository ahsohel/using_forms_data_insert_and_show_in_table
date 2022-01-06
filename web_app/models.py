from django.db import models

# Create your models here.

class form_models(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ' ' + self.phone

