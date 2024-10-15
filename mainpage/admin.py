from django.contrib import admin

from mainpage.models import PersonalInfo, AdditionalInfo


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    pass