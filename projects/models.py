from django.db import models


class Portafolio(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    author = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, editable=True)
    wrapper_img = models.ImageField(upload_to='projects/wrapper')
    modal_img = models.ImageField(upload_to=' projects/modal')
    published = models.BooleanField(default=False)
