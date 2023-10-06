from django.contrib import admin
from course.models import Student
# Register your models here.
class SAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city','marks']
    list_filter = ['city']
    search_fields = ['name','city']
admin.site.register(Student,SAdmin)    # Registering the model Student
