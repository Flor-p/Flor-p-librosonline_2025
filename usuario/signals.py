from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from usuario.models import Datosusuario

@receiver(post_save, sender=User)
def create_or_update_datosusuario(sender, instance, created, **kwargs):
    """
    Create or update Datosusuario profile when a User instance is created or updated.
    """
    if created:
        Datosusuario.objects.get_or_create(usuario=instance)  # Ensure only one profile per user
        print("Datosusuario profile created.")
    else:
        instance.perfil.save()  # Access using related_name="perfil"
        print("Datosusuario profile updated.")
