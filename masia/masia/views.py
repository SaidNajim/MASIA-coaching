from django.shortcuts import render, redirect

from .models import Entrepreneur, Activity, City
from django.contrib import messages
from django.core.paginator import Paginator
import traceback

def index(request):
    entrepreneurs = Entrepreneur.objects.filter().order_by("-pk")
    skills = ["Tenis", "Football"]
    page_num = request.GET.get("page", 1)
    p = Paginator(entrepreneurs, 12)
    entrepreneurs = p.get_page(page_num)
    context = {
        "entrepreneurs": entrepreneurs,
        "skills": skills,
        "cities": ["Temara", "Salé"],
        "page_title": "Trouver un coach",
        "page_id": 5,
    }
    return render(request, "masia/index.html", context)

def clean_filters(filters):
    filters = {k: v for k, v in filters.items() if v}
    return filters

def search(request):
    filters = {
        "user__first_name__icontains": request.GET.get("fname_kw"),
        "user__last_name__icontains": request.GET.get("lname_kw"),
        "activity1__name__icontains": request.GET.get("activity_kw"),
        "city__name__icontains": request.GET.get("city_kw"),
    }

    html_queries = {
        "fname_kw": request.GET.get("fname_kw"),
        "lname_kw": request.GET.get("lname_kw"),
        "activity_kw": request.GET.get("activity_kw"),
        "city_kw": request.GET.get("city_kw"),
    }

    filters = clean_filters(filters)
    html_queries = clean_filters(html_queries)

    entrepreneurs = Entrepreneur.objects.filter(**filters)

    page_num = request.GET.get("page", 1)
    p = Paginator(entrepreneurs.order_by("-pk"), 12)
    entrepreneurs = p.get_page(page_num)

    context = {
        "entrepreneurs": entrepreneurs,
        "activities": Activity.objects.all(),
        "cities": City.objects.all(),
        "filters": html_queries,
        "page_title": "Trouver un coach",
        "page_id": 5,
    }
    return render(request, "masia/index.html", context)


def send_rfq(request, id):
    try:
        entrepreneur = Entrepreneur.objects.get(id=id)
        print(entrepreneur)
        context = {
            "e": entrepreneur,
            "page_title": "Profil coach",
        }
        return render(request, "masia/coach.html", context)
    except:
        print("EXCEPTION: ", traceback.format_exc())

def apply(request):
    context = {
        "page_title": "Devenir Coach",
    }
    return render(request, "masia/apply.html")
