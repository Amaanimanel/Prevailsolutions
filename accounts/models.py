from sre_constants import CATEGORY
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings

class Investor(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    cv = models.FileField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.name)



class Investment(models.Model):
    TYPEOFPOS = (
            ('Full-time', 'Full-time'),
            ('Part-time', 'Part-time'),
            ('Temporal', 'Temporal'),
            ('Permanent', 'Permanent'),
            ('contract', 'contract'),
            )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    investor = models.ForeignKey(Investor, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=200, null=True)
    State = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    industry = models.CharField(max_length=200, null=True)
    typeofpos = models.CharField(default='Full-time', max_length=200, null=True, choices=TYPEOFPOS)
    amount = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(100),                                                                       MaxValueValidator(900000)], null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.amount) 

