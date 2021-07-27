from django.urls import path
from . import views
# URLCONF MODULE

urlpatterns = [
    path('', views.home, name="home"),
    path('resume/', views.resume, name="resume"),
    path('creations/', views.creations, name="creations"),
    path('aboutme/', views.about_me, name="aboutme"),

    # EMAIL
    path('sent/', views.sendEmail, name='send_email'),
]
