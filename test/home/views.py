from django.shortcuts import render, HttpResponse, redirect
from django.db import connection
from .models import R21, UserModel
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from .scrap import forcesrate, coderate, leetrate, spojrate
# Create your views here.


def admin_panel(request):
    return render(request, 'adminpanel.html')


def hod_panel(request):
    return render(request, 'hod_panel.html')


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = UserModel.objects.get(username=username, password=password)
            if user.user_type == "admin":
                return redirect('admin_panel')
            elif user.user_type == "hod":
                return redirect('hod_panel')
        except UserModel.DoesNotExist:
            pass

    return render(request, 'login.html')


def display_students(request, year, br):
    if (year == '3rd'):
        if (br != 'all'):
            students = R21.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R21.objects.all().order_by('-overall_score')
    if (year == '2nd'):
        if (br != 'all'):
            students = R22.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R22.objects.all().order_by('-overall_score')
    if (year == '1st'):
        if (br != 'all'):
            students = R23.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R23.objects.all().order_by('-overall_score')

    if (year == '4th'):
        if (br != 'all'):
            students = R20.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R20.objects.all().order_by('-overall_score')

    return students
    # return render(request,'display.html',context)

    ''' with connection.cursor() as cursor:
        cursor.callproc('get_det')
        results = cursor.fetchall()
        print(results)
    '''


def validate(request):
    if request.method == 'POST':
        details = request.POST.dict()
        year = details['year']
        branch = details['branch']
        print(year, branch)

        students = display_students(request, year, branch)
        context = {
            'students': students
        }
        return render(request, 'display.html', context)


def update(request):
    students = R21.objects.all().values()

    for i in students:

        roll = i['roll_number']
        print(roll, end="---")
        cc_id = i['codechef_username']
        cf_id = i['codeforces_username']
        spoj_id = i['spoj_username']

        cc_prob = coderate(cc_id)
        cf_prob = forcesrate(cf_id)
        # spoj_prob=spojrate(spoj_id)

        stu = R21.objects.get(roll_number=roll)
        stu.cc_problems_solved = cc_prob
        stu.cf_problems_solved = cf_prob
        stu.total_ccps_10_field = cc_prob*10
        stu.total_cfps_10_field = cf_prob*10
        stu.save()
    context = {
        'updated': 'updated'
    }
    return render(request, 'updating.html', context)
