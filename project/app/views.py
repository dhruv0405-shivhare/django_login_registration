from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
         name=request.POST.get('username') 
         email=request.POST.get('email')
         detail=request.POST.get('detail')
         contact=request.POST.get('phone')
         dob=request.POST.get('dob')  
         edu=request.POST.getlist('subscribe')
         gender=request.POST.getlist('gender')
         image=request.FILES.get('profile-pic')  
         resume=request.FILES.get('resume') 
         password=request.POST.get('password')
         cpassword=request.POST.get('cpassword')   
        #  print(name,email,detail,contact,dob,edu,gender,image,resume,password,cpassword) 
         
         user= Student.objects.filter(email=email)
         if user:
             x='Email Already Exist'
             return render(request,'register.html',{'msg':x})
         else:
              if password==cpassword:
                  Student.objects.create(name=name,email=email,detail=detail,phone=contact,subscribe=edu,dob=dob,gender=gender,profile_pic=image,resume=resume,password=password)
                  x="Registration Sucessfully"
                  return render(request,'login.html',{'msg':x})
              else:
                  x="Password and cpassword Not Match"
                  return render(request,'register.html',{'msg':x,'name':name,'email':email,'detail':detail,'phone':contact,'subsribe':edu,'dob':dob,'gender':gender,'profile_pic':image,'resume':resume})
                  
    else:
         return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=Student.objects.filter(email=email)
        if user:
            data=Student.objects.get(email=email)
            user_data={
                'name':data.name,
                'email':data.email,
                'phone':data.phone,
                'dob':data.dob,
                'subscribe':data.subscribe,
                'gender':data.gender,
                'profile_pic':data.profile_pic,
                'resume':data.resume,

            }
            print(user_data)
            # print(data.email)
            # print(data.detail)
            # print(data.dob)
            # print(data.gender)
            # print(data.profile_pic)
            # print(data.resume)
            # print(data.subscribe)
            # print(data.phone)
            # print(data.password)
            # print(data.name)
            pass1= data.password
            if pass1 == password:
                return render(request,'dashboard.html',{'name':data.name,'email':data.email})
            else:
                msg = "Enter and Password not Match"
                return render(request,'login.html',{'msg':msg})
        else:
            msg = "Email not Exist"
            return render(request,'register.html',{'msg':msg})    
    else:
        return render(request,'login.html')