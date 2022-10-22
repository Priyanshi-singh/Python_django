from django.contrib import admin
from .models import Movies, Show, Student,Report, Weather 
# Register your models here.

admin.site.register(Movies)   #this line add tables to admin dashboard
admin.site.register(Show)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin)
