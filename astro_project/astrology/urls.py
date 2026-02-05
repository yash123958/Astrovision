from django.urls import path
from .views import home, daily_horoscope, weekly_horoscope,contact,blog,signup

app_name = "astrology"

urlpatterns = [
    path("", home, name="home"),
    path("daily-horoscope/", daily_horoscope, name="daily_horoscope"),
    path("weekly-horoscope/", weekly_horoscope, name="weekly_horoscope"),
    path("contact/", contact, name="contact"),
    path("blog/", blog, name="blog"),
     path('signup/', signup, name='signup'),

]
