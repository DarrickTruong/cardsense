from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import time
import datetime
import bcrypt


def login(request):
    return render(request, 'login_register/login.html')

def login_valid(request):
    print("in login valid")
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        print(logged_user.id)
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            print(logged_user.first_name)
            return redirect('/dashboard')
            # ** redirect after POST**
        else:
            messages.error(request, "Email and Password do not match or do not exist.")
            # print('in else error **')
            return render(request, 'login_register/login.html')
    else:
            messages.error(request, "Email and Password do not match or do not exist.")
            return redirect('/login')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        request.session.modified=True
        # print('user_id deleted')
    return redirect('/')

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value, extra_tags="create")
        return redirect('/login')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        # print('pw_hash', pw_hash)
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], phone=request.POST['phone'], birthday=request.POST['birthday'], password=pw_hash)
        request.session['user_id'] = User.objects.last().id
    return redirect('/final_setup')

def final_setup(request):
    user = User.objects.get(id=request.session['user_id'])
    # print('this is created user', user)
    return render(request, "login_register/final_setup.html")

def process_setup(request):
    user = User.objects.get(id=request.session['user_id'])
    # # print('this is last user', user)
    # errors = User.objects.socialvalidate(request.POST)
    # if len(errors) > 0:
    #     print('this is error in process_setup')
    #     for key, value in errors.items():
    #         messages.error(request, value, extra_tags=key)
    #     return redirect('/final_setup')
    # else:
    #     print('this is last user', user)
    #     user = User.objects.last()
    #     user.linkedin = request.POST['linkedin']
    #     user.facebook = request.POST['facebook']
    #     user.instagram = request.POST['instagram']
    #     user.website = request.POST['website']
    #     user.profile_pic = request.FILES['profile_pic']
    #     user.save()
    # return redirect('/dashboard')
    # print('this is last user', user)
    # user = User.objects.last()
    user.linkedin = request.POST['linkedin']
    user.facebook = request.POST['facebook']
    user.instagram = request.POST['instagram']
    user.website = request.POST['website']
    user.profile_pic = request.FILES['profile_pic']
    user.save()
    return redirect('/dashboard')
