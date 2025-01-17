from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.admin import AdminSite

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )


class CustomAdminSite(AdminSite):
    site_header = "Taomxona Boshqaruvi"
    site_title = "Admin Panel"
    index_title = "Xush kelibsiz"

    def each_context(self, request):
        context = super().each_context(request)
        context['css_files'] = [
            'admin/css/custom.css',  
        ]
        return context

admin_site = CustomAdminSite(name='custom_admin')

from .models import Dish, Category

admin_site.register(Dish)
admin_site.register(Category)
