from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display=['Pid','name','age']

class UserAdmin(admin.ModelAdmin):
    list_display = ['P_id', 'Ansid']

class UserAdmin(admin.ModelAdmin):
    list_display=['Qid','Question']

class UserAdmin(admin.ModelAdmin):
    list_display = ['Q_id', 'Ansid', 'Answers']


# Register your models here.
admin.site.register(Patient)
admin.site.register(Answer)
admin.site.register(QuesAns)
admin.site.register(Results)
# Register your models here.
