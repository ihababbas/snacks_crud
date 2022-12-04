from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse 
# Create your models here


class Snack (models.Model):
    name = models.CharField(max_length=64, help_text="thing name", default="thing")
    purchaser =models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    desc= models.TextField(default="description")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "my snacks"   
        ordering=['pk']

    def get_absolute_url(self):
        return reverse('thing_detail',args=[self.id])