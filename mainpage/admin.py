from django.contrib import admin

from mainpage.models import PersonalInfo


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    pass