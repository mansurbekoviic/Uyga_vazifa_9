from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from menu.models import Dish

class Command(BaseCommand):
    help = 'Create a user and add permissions'

    def handle(self, *args, **kwargs):
        user = User.objects.create_user(username='john', password='password123')
        content_type = ContentType.objects.get_for_model(Dish)
        permission = Permission.objects.get(codename='add_dish', content_type=content_type)
        user.user_permissions.add(permission)
        self.stdout.write(self.style.SUCCESS('User and permissions added successfully.'))
