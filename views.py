from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request,'layout.html',{'name':'govind'})


def StudForm(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            r = form.cleaned_data['regNo']
            c = form.cleaned_data['classs']
            s = Student()
            s.name = n
            s.regNo = r
            s.classs = c
            s.save(using = 'mdb')
            return HttpResponseRedirect('/schoolapp/form')
    else:
        sform = StudentForm()
        return render(request,'layout.html',{'fm':sform})
        

def TeachForm(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            e = form.cleaned_data['empId']
            s = form.cleaned_data['sub']
            t = Teacher()
            t.name = n
            t.empId = r
            t.sub = c
            t.save(using = 'mdb')
            return HttpResponseRedirect('/schoolapp/form')
    else:
        sform = StudentForm()
        return render(request,'layout.html',{'fm':sform})
    
    
def mydb(request):
    s = Student.objects.all()
    
    return render(request,'layoutone.html',{"d":s})


# Create your views here.
