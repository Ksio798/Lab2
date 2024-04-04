from django.contrib import admin
from .models import *

admin.site.register(Teachers)
admin.site.register(Students)
admin.site.register(Grades)
admin.site.register(Hometasks)
admin.site.register(Classes)
admin.site.register(Schedules)

