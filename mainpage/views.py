from django.shortcuts import render

from .models import *


def main_banner(request):
    main_info = PersonalInfo.objects.all()
    additional = AdditionalInfo.objects.all()
    experience = Experience.objects.all()
    work_experience = WorkExperience.objects.all()
    portfolio = Portfolio.objects.all()
    leadership = WorkExperience.objects.filter(leadership=True)
    return render(
        request,
        "base.html",
        {
            "main_info": main_info,
            "additional": additional,
            "experience": experience,
            "work_experience": work_experience,
            "leadership" : leadership,
            "portfolio": portfolio
        }
    )