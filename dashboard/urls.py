from django.urls import path, include
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard, name = 'dashboardIndex'),
    path('staff/', views.staff_list, name = 'staff_list'),
    path('attendence/', views.attendence, name = 'attendence'),
    path('staff/create/', views.staff_create, name = 'staff_create'),
    path('staff/delete/<int:id>/', views.staff_delete, name="staff_delete"),
    path('staff/update/<int:id>/', views.staff_update, name="staff_update"),
    path('attendence/start/', views.attendence_start, name="attendence_start"),
    path('profile', views.profile, name="profile")
]
