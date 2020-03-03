from django.contrib import admin
from .models import person_inquir

# Register your models here.
class Person_inquirAdmin(admin.ModelAdmin):
    list_display=(
        'created','first_name','last_name','phone_number','email','message','usa','australia','canada','united_kingdom',
    )


admin.site.register(person_inquir,Person_inquirAdmin)
