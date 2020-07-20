from django.db import models


TECH_CHOICES = (
    ('WordPress', 'WordPress'),
    ('Woocommerce', 'Wocommerce'),
    ('Majento', 'Majento'),

)

# Create your models here.
class Companies(models.Model):
    url = models.CharField(max_length=200, null=True)
    tech = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.url



 
