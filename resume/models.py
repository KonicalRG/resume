from django.db import models


class EmploymentHistory(models.Model):
    '''
    Model class for Employment History
    '''
    title = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    main_role = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title + " " + self.role


class AcademicTraining(models.Model):
    '''
    Model class for Academy Training
    '''
    college = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.college + " " + self.title
