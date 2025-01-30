from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        print(request.POST)
        name=request.POST.get('username')
        email=request.POST.get('email')
        detail=request.POST.get('detail')
        phone=request.POST.get('phone')
        dob=request.POST.get('dob')
        profile_pic=request.FILES.get('profile-pic')
        resume=request.FILES.get('resume')
        password=request.POST.get('password')
        repassword=request.POST.get('cpassword')
        gender=request.POST.get('gender')
        user=Student.objects.filter(email=email)
        # print(name)
        # print(email)
        # print(phone)
        # print(detail)
        # print(dob)
        # print(profile_pic)
        # print(resume)
        print(password)
        print(repassword)
        # print(gender)
        if user:
            msg="Email already exist"
            return render(request,'register.html',{'msg':msg})
        
        else:
            if password == repassword:
                Student.objects.create(name='name',email='email',phone='phone',detail='detail',dob='dob',profile_pic='profile_pic',resume='resume',password='password',gender='gender')
                msg="registration successfully"
                return render(request,'login.html',{'msg':msg})
            else:
                msg="password and repassword not match"
                return render(request,'register.html',{'msg':msg,'name':name,'email':email,'phone':phone,'detail':detail,'dob':dob,'profile_pic':profile_pic,'resume':resume,'gender':gender})
    else:
        return render(request,'register.html')  

def login(request):
    return render(request,'login.html')