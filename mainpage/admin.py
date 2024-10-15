from django.contrib import admin

from mainpage.models import PersonalInfo, AdditionalInfo, Experience


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass