from django.core import validators
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentsRegistations
from .models import User

# Create your views here.


# this function will add user and shows user
def add_show(request):
    if request.method == 'POST':
        fm = StudentsRegistations(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentsRegistations()
    else:
        fm = StudentsRegistations()
    stud = User.objects.all()
    return render(request,"enroll/addandshow.html",{'form':fm,'stu':stud})

# this function update/edit user
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentsRegistations(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentsRegistations(instance=pi)
    return render(request,"enroll/updatestudents.html",{'form':fm})


# this  function delete user 
def delete_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')