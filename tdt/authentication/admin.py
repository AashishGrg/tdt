from django.contrib import admin
from .models import User,AdminUser,NormalUser
# Register your models here.
admin.site.register(User)
admin.site.register(AdminUser)
admin.site.register(NormalUser)