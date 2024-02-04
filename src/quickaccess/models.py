from django.db import models

# Create your models here.
class MMDQuickFavorites(models.Model):
    Username = models.CharField(max_length=100, default='', blank=False, null=False, primary_key=True)
    AccessKey = models.CharField(max_length=100, default='', blank=False, null=False)
    Data = models.JSONField(default=dict, blank=False, null=False)