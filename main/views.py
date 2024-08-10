from django.shortcuts import render
from main.models import Employee, Attendance
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from main.models import ADMIN, STAFF



@login_required
def dashboard(request):
    attendences = Attendance.objects.filter(employee=request.user)

    if len(attendences) > 5:
        attendences = attendences[0:5]

    context = {
        'title':'Dashboard',
        'attendences': attendences
    }
    return render(request, 'main/index.html', context)


def attendence(request):
    attendences = Attendance.objects.filter(id=request.user.id)

    context = {
        'title': "Davomat jadvali",
        'attendences': attendences
    }
    return render(request, 'main/attendence.html', context)



def profile(request):
    user = Employee.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        
        password = request.POST.get('password')
        if password:  
            user.password = make_password(password) 
        user.save()

    context = {
        'title':"My Profile",
        'user': user,
    }
    
    return render(request, 'main/profile.html', context)
  









