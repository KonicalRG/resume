from django.db import models


class EmploymentHistory(models.Model):
    title = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title + " " + self.role


class AcademicTraining(models.Model):
    college = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.college + " " + self.title

