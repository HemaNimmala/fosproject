from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Jobdetails(models.Model):
    work_title=models.CharField(max_length=225)
    #salary_offered=models.DecimalField(max_digits=10,decimal_places=2,null=False)
    salary_offered=models.CharField(max_length=225)

    Job_type=[
        ('fulltime','Full-Time'),
        ('parttime', 'part-Time'),
        ('selling','Selling'),
    ]

    job_type=models.CharField(max_length=20,choices=Job_type)
    age = models.IntegerField()
    skills=models.TextField()
    education=models.CharField(max_length=255)



    #
    # def __str__(self):
    #     return self.work_title
