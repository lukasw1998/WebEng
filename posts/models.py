from django.db import models

# Create your models here.

class Notice(models.Model):
    notice_title = models.CharField(max_length=80)
    notice_text = models.CharField(max_length=400)
    pub_start = models.DateTimeField()
    pub_end = models.DateTimeField()