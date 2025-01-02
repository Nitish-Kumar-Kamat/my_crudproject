from django.shortcuts import render,redirect
from django.http import HttpResponse
from crud.models import Students

def home(req):
	return render(req,"home.html")

def insert(req):
	return render(req,"insert.html")

def insertTask(req):
	if req.method=="POST":
		n=req.POST.get('name')
		ln=req.POST.get('lname')
		em=req.POST.get('email')
		ag=req.POST.get('age')
		img=req.FILES.get('img')
		data=Students(name=n,lname=ln,email=em,age=ag,image=img)
		data.save()
	return redirect('/display')

def display(req):
	data=Students.objects.all()
	return render(req,"display.html",{'data':data})

def delete(req):
	data=Students.objects.all()
	return render(req,"delete.html",{'data':data})

def deleterec(req,id):
	data=Students.objects.get(id=id)
	data.delete()
	return redirect('/delete')

def update(req):
	data=Students.objects.all()
	return render(req,"update.html",{'data':data})

def updatedata(req,id):
	if req.method=="POST":
		n=req.POST.get('name')
		ln=req.POST.get('lname')
		em=req.POST.get('email')
		ag=req.POST.get('age')
		im=req.FILES.get('img')
		if im==None:
			Students.objects.filter(id=id).update(name=n,lname=ln,email=em,age=ag)
			return redirect('/update')
		else:
			data=Students(id=id,name=n,lname=ln,email=em,age=ag,image=im)
			data.save()
			return redirect('/update')
	data=Students.objects.get(id=id)
	return render(req,"updatedata.html",{'data':data})

