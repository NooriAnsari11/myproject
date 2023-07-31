from django.contrib import admin
from .models import Student,UserProgress,UserProfile,Badge,UserBadge
# Register your models here.

admin.site.register(Student)
admin.site.register(UserProgress)
admin.site.register(UserProfile)
admin.site.register(Badge)
admin.site.register(UserBadge)
