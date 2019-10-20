from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    suject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):

        return self.name + self.email + self.suject

    def get_absolute_url(self):

        # return reverse_lazy("index")
        return reverse("index")
