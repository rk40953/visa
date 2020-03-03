from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import person_inquir
from django.core.mail import send_mail
from django.template.loader import get_template

# Create your views here.


def home(request):
    return render (request,'home.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login/')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email = request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        username=request.POST['username']

        if password1==password2:

            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register/')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register/')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,frist_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'User created')
                return redirect('/')

        else:
            messages.info(request,'password is not matched')
            return render(request,'register.html')

def person_inquiry(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        message=request.POST.get('message')
        usa=request.POST.get('usa')
        australia=request.POST.get('australia')
        canada=request.POST.get('canada')
        united_kingdom=request.POST.get('united_kingdom')

        subject='Contact From Received'
        from_email=settings.DEFAULT_FROM_EMAIL
        to_email=[settings.DEFAULT_FROM_EMAIL]

        context = {
            'first_name':first_name,
             'last_name':last_name,
             'email':email,
            'phone_number':phone_number,
            'message':message,
            'usa':usa,
            'australia':australia,
            'canada':canada,
            'united_kingdom':united_kingdom,

               }
        contact_message=get_template('contact_message.txt').render(context)
        send_mail(subject,contact_message,from_email,to_email,fail_silently=True)

        person=person_inquir.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,message=message,usa=usa,canada=canada,australia=australia,united_kingdom=united_kingdom)
        person.save()
        messages.info(request,'inquiry form submitted sucessfully')
        return redirect('/')
    else:
        return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect("/")