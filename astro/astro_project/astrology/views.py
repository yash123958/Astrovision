from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .utils import (
    get_zodiac_sign,
    get_prediction,
    time_category,
)
from .models import BirthDetail


# ================= HOME =================
@login_required
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        birth_date = request.POST.get("birth_date")
        birth_time = request.POST.get("birth_time")

        day = int(birth_date.split("-")[2])
        month = int(birth_date.split("-")[1])

        zodiac = get_zodiac_sign(day, month)
        prediction = get_prediction(zodiac)
        born_time = time_category(birth_time)

        BirthDetail.objects.create(
            name=name,
            birth_date=birth_date,
            birth_time=birth_time
        )

        return render(
            request,
            "astrology/result.html",
            {
                "name": name,
                "zodiac": zodiac,
                "prediction": prediction,
                "born_time": born_time
            }
        )

    return render(request, "astrology/index.html")



# ================= AUTH =================

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   # goes to /accounts/login/
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


@login_required
def welcome(request):
    return render(request, "astrology/index.html")


# ================= OTHER PAGES =================

def daily_horoscope(request):
    return render(request, "astrology/daily_horoscope.html")


def weekly_horoscope(request):
    return render(request, "astrology/weekly_horoscope.html")


def contact(request):
    return render(request, "astrology/contact.html")


def blog(request):
    return render(request, "astrology/blog.html")
