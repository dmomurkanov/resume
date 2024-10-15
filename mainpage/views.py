from django.shortcuts import render

from .models import PersonalInfo


def main_banner(request):
    main_info = PersonalInfo.objects.fisrt()
    return render(
        request,
        "mainbanner.html",
        {
            "main_info": main_info
        }
    )