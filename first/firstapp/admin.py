from django.contrib import admin

from firstapp.models import Student

# Register your models here.
class sadmi(admin.ModelAdmin):
    list_display=('name','roll')

admin.site.register(Student,sadmi)
