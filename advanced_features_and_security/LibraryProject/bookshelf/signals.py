from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.label != "bookshelf":
        return

    viewers, _ = Group.objects.get_or_create(name="Viewers")
    editors, _ = Group.objects.get_or_create(name="Editors")
    admins, _ = Group.objects.get_or_create(name="Admins")

    perms = Permission.objects.filter(codename__in=[
        "can_view", "can_create", "can_edit", "can_delete"
    ])

    viewers.permissions.set(perms.filter(codename="can_view"))
    editors.permissions.set(perms.filter(codename__in=["can_view", "can_create", "can_edit"]))
    admins.permissions.set(perms)  # all permissions
