from django.shortcuts import render
from .models import UserProfileInfo
from .forms import UserProfileInfoForm, UserForm
from django.urls import reverse
from django.contrib.auth import  authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    index_dic = {
        'greeting':'Hello !! Welcome to my django lv five !'
    }
    return render(request,'lvfive_app/index.html',context=index_dic)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm (data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errrors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'lvfive_app/registration.html',{'user_form' : user_form,
        'profile_form': profile_form,
        'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username : {}, and Password : {}".format(username,password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'lvfive_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice !!")
# def user(request):
#     userdata = User.objects.order_by('first_name')
#     user_dic={
#         'userdata' : userdata,
#         'heading':'USER INPUT'
#     }
#     return render(request,'lvfive_app/user.html',context=user_dic)

# def UserForm(request):
#     user_form = NewUserForm()
#
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#         else:
#             print("Sorry this is an error")
#     userdata = UserInput.objects.order_by('first_name')
#     user_dic={
#         'userdata' : userdata,
#         'user_form' : user_form,
#         'greeting' : 'USER INPUT',
#     }
#     return render(request,'lvfive_app/user.html',context=user_dic)
