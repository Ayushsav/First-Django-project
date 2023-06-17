from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
#for file uploading
from django.core.files.storage import FileSystemStorage
#for display image
from django.conf import settings
media_url=settings.MEDIA_URL

def home(request):
    return render(request,"home.html")

def register(request):
    if request.method=="POST":
        fnm=request.POST.get("fnm")
        mno=request.POST.get("mno")
        emailid=request.POST.get("emailid")
        pwd=request.POST.get("pwd")
        role="student"
        obj=models.mstuser(fnm=fnm,mno=mno,emailid=emailid,pwd=pwd,role=role)
        obj.save()
        return render(request,"register.html")
    else:
        return render(request,"register.html")

def userlist(request):
    res=models.mstuser.objects.filter(role="student")
    return render(request,"userlist.html",{'res':res})

def login(request):
    if request.method=="POST":
        emailid=request.POST.get("emailid")
        pwd=request.POST.get("pwd")
        res=models.mstuser.objects.filter(emailid=emailid,pwd=pwd)
        if len(res)>0:
         role=res[0].role
         #for creating session
         request.session['emailid']=emailid
         request.session['role']=role
         #-------------------------------------
         print(role)
         if role=="admin":
             print("Welcome Admin")
             return redirect("/adminhome/")
         else:
             return redirect("/studenthome/")
        return render(request,"home.html")
    else:
        return render(request,"login.html")
       
def adminhome(request):
    return render(request,"adminhome.html")
        
def addcourse(request):
    if request.method=="POST":
        nm=request.POST.get("nm")
        duration=request.POST.get("duration")
        fees=request.POST.get("fees")
        #for file uploading
        courseicon=request.FILES["courseicon"]
        fs=FileSystemStorage()
        courseimg=fs.save(courseicon.name,courseicon)
        obj=models.course(nm=nm,duration=duration,fees=fees,courseicon=courseicon)
        obj.save()
        return render(request,"addcourse.html")
    else:
     return render(request,"addcourse.html")


def courselist1(request):
    res=models.course.objects.all()
    return render(request,"courselist1.html",{'res':res,'media_url':media_url})

def addbatch(request):
    if request.method=="POST":
        nm=request.POST.get("nm")
        startdate=request.POST.get("startdate")
        batchtime=request.POST.get("batchtime")
        facultyname=request.POST.get("facultyname")
        obj=models.batch(nm=nm,startdate=startdate,batchtime=batchtime,facultyname=facultyname)
        obj.save()
        return render(request,"addbatch.html")
    else:
        return render(request,"addbatch.html")
    
def studenthome(request):
    return render(request,"studenthome.html")

# def logout(request):
#     return redirect("/home.html")

def batchlist1(request):
    res=models.batch.objects.all()
    return render(request,"batchlist1.html",{'res':res,})

def batchlist2(request):
    res=models.batch.objects.all()
    return render(request,"batchlist2.html",{'res':res,})

def courselist2(request):
    res=models.course.objects.all()
    return render(request,"courselist2.html",{'res':res,'media_url':media_url})