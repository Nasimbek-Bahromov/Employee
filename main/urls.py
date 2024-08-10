from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.dashboard, name = 'index'),
    path('attendence/', views.attendence, name = 'attendence'),
    path('profile', views.profile, name="profile")
]
