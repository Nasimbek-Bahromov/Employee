from django.shortcuts import render, redirect
from main.models import Employee, Attendance
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from main.models import ADMIN, STAFF
import datetime



@login_required
def dashboard(request):
    employees = Employee.objects.filter(is_staff= STAFF)
    attendences = Attendance.objects.all()
    if len(employees) > 5:
        employees = employees[0:5]

    if len(attendences) > 5:
        attendences = attendences[0:5]

    context = {
        'title':'Dashboard',
        'employees': employees,
        'attendences': attendences
    }
    return render(request, 'dashboard/index.html', context)

def staff_list(request):
    employees = Employee.objects.filter(is_staff= STAFF)

    context = {
        'title':"Xodimlar ro'yxati",
        'employees': employees,
    }
    return render(request, 'dashboard/staff_list.html', context)

def attendence(request):
    attendences = Attendance.objects.all()

    context = {
        'title': "Davomat jadvali",
        'attendences': attendences
    }
    return render(request, 'dashboard/attendence.html', context)


    
def staff_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))  
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        salary = request.POST.get('salary')
        workplace = request.POST.get('workplace')
        position = request.POST.get('position')
        age = request.POST.get('age')

        try:
            Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                gender=gender,
                phone=phone,
                salary=salary,
                workplace=workplace,
                position=position,
                age=age,
                is_staff=STAFF,
            )
        except: 
            context = {
                'title':"Xodim yaratish"
            }
            
            return render(request, 'dashboard/staff_create.html', context) 

        return redirect('dashboard:staff_list') 
    
    context = {
        'title':"Xodim yaratish",
    }
    
    return render(request, 'dashboard/staff_create.html', context) 


def staff_update(request, id):
    try:
        employee = Employee.objects.get(id=id)  
    except Employee.DoesNotExist:
        return redirect('dashboard:staff_list') 

    if request.method == 'POST':
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.username = request.POST.get('username')
        
        password = request.POST.get('password')
        if password:  
            employee.password = make_password(password)
        
        employee.gender = request.POST.get('gender')
        employee.phone = request.POST.get('phone')
        employee.salary = request.POST.get('salary')
        employee.workplace = request.POST.get('workplace')
        employee.position = request.POST.get('position')
        employee.age = request.POST.get('age')
        
        employee.save()  
        return redirect('dashboard:staff_list')

    return render(request, 'dashboard/staff_update.html', {'employee': employee})

def attendence_start(request):

    employees = Employee.objects.filter(is_staff= STAFF)

    if request.method == 'POST':
        id = request.POST.get('employee_id')
        status = request.POST.get('status')

        present = True if status == 'on' else False
        
        Attendance.objects.create(
            employee=Employee.objects.get(id=id),
            present = present,
            arrival_time=datetime.datetime.now()
        )
        return redirect('dashboard:attendence')

    context = {
        'title':"Davomat olish",
        'employees': employees,
    }

    return render(request, 'dashboard/attendence_start.html', context)


def profile(request):
    admin = Employee.objects.get(id=request.user.id)
    if request.method == 'POST':
        admin.first_name = request.POST.get('first_name')
        admin.last_name = request.POST.get('last_name')
        admin.username = request.POST.get('username')
        
        password = request.POST.get('password')
        if password:  
            admin.password = make_password(password) 
        admin.gender = request.POST.get('gender')
        admin.phone = request.POST.get('phone')
        admin.age = request.POST.get('age')
        admin.save()

    context = {
        'title':"My Profile",
        'admin': admin,
    }
    
    return render(request, 'dashboard/profile.html', context)
      


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if request.user.is_staff == ADMIN:
                return redirect('dashboard:dashboardIndex')
            return redirect('main:index')
        else:
            context = {'error': 'Invalid username or password.'}
            return render(request, 'dashboard/login.html', context)
    return render(request, 'dashboard/login.html')



def log_out(request):
    logout(request)
    return redirect('login_user')

def staff_delete(request, id):
    Employee.objects.get(id = id).delete()

    return redirect('dashboard:staff_list')






