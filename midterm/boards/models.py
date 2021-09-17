from django.db import models

# Create your models here.
class BoardTab(models.Model):
    name = models.CharField(max_length = 20)
    #passwd = models.CharField(max_length = 20)
    title = models.CharField(max_length = 100)
    cont = models.TextField()
    bdate = models.DateTimeField()
    readcnt = models.IntegerField()
    gnum = models.IntegerField()
    onum = models.IntegerField()
    nested = models.IntegerField()
    type = models.CharField(max_length = 10)