from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Store

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_store_for_owner(sender, instance, created, **kwargs):
    # If user is created and role is Business Owner (example role name)
    if created and instance.role and instance.role.name.lower() == 'business owner':
        Store.objects.create(owner=instance, name=f"{instance.username}'s store")
