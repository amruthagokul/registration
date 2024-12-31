from django.shortcuts import render,redirect
from.models import*
# Create your views here.
def form(request):
    return render(request,"form.html")
def stud(request):
    if request.method=="POST": 
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        age=request.POST['age']
        course=request.POST["course"]
       
        data=student(email=email,name=name,phone=phone,age=age,course=course)
        data.save()
    return redirect('form')
def table(request):
    data=student.objects.all()
    return render(request,"table.html",{'data':data})
