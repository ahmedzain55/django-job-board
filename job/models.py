from django.db import models


# Create your models here.

class Job(models.Model):
    choices1 = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]

    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=30, choices=choices1)
    description = models.TextField(max_length=1000, null=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title



