from django.db import models

class Recruiter(models.Model):
    tech_stack = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
