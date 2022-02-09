from django.shortcuts import render, HttpResponseRedirect
from Registration.form import StuRegistration
from Registration.models import RegistrationStu

# Create your views here.
#This method will add new Items and Show all Items
def entryandshow(request):
    
    if(request.method=='POST'):
        
        fm=StuRegistration(request.POST)
        if(fm.is_valid()):
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=RegistrationStu(name=nm,email=em,password=pw)
            reg.save()
            fm=StuRegistration()
        
    else:
        fm=StuRegistration()
    stud=RegistrationStu.objects.all()
        
   
    return render(request,'entryandshow.html',{'form':fm,'stu':stud})

#this method is for update

def update_data(request,id):
    
    if(request.method=='POST'):
        pi=RegistrationStu.objects.get(pk=id,)
        fm=StuRegistration(request.POST, instance=pi)
        if(fm.is_valid):
            fm.save()
    else:
        pi=RegistrationStu.objects.get(pk=id,)
        fm=StuRegistration(instance=pi)

    return render(request, 'update.html',{'form':fm})

    

 #This function will delete

def delete_data(request,id):
    if(request.method=='POST'):
        pi=RegistrationStu.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')


