from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group



from .models import Investor



def investor_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='investor')
        instance.groups.add(group)            
        
        Investor.objects.create(
            user=instance,
            name=instance.username,
            )

post_save.connect(investor_profile, sender=User)


