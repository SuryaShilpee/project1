# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import redirect


from django.shortcuts import render, redirect
# Create your views here.
from project1.models import Project1


def home(request):

    data = Project1.objects.all()

    return render(request, 'project1/home.html',
                  {'data': data})


def insert_data(request):

    return render(request, 'project1/insert_data.html')


def updated_data(request):

    count = request.POST.get('count')
    c = int(count)
    x = c+1
    insert_list = []
    for i in range(1, x):

        name = request.POST.get('name'+str(i))
        age = request.POST.get('age'+str(i))
        address1 = request.POST.get('address1'+str(i))
        address2 = request.POST.get('address2'+str(i))
        city = request.POST.get('city'+str(i))
        state = request.POST.get('state' + str(i))
        insert_list.append(Project1(name=name, age=age, address1=address1, address2=address2, city=city, state=state))

    Project1.objects.bulk_create(insert_list)
    return redirect('/project1/home/')


def updated_data2(request):

    count = request.POST.get('count')
    c = int(count)
    x = c+1

    insert_list = []
    for i in range(1, x):
        if 'name'+str(i) in request.POST:

            name = request.POST.get('name' + str(i))
            age = request.POST.get('age' + str(i))
            address1 = request.POST.get('address1' + str(i))
            address2 = request.POST.get('address2' + str(i))
            city = request.POST.get('city' + str(i))
            state = request.POST.get('state' + str(i))

            insert_list.append(Project1(name=name, age=age, address1=address1, address2=address2, city=city, state=state))

    Project1.objects.bulk_create(insert_list)
    return redirect('/project1/home/')
