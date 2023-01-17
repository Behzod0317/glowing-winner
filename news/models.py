from django.db import models

# Create your models here.

class News(models.Model):

    name = models.CharField("Yangilik nomi",max_length=250)
    text = models.TextField("Yangilik matni")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Yangilik"
        verbose_name_plural = "Yangiliklar"