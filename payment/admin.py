from django.contrib import admin
from .models import User,Balance,Credit

admin.site.register(User)
admin.site.register(Balance)
admin.site.register(Credit)

# Register your models here.
