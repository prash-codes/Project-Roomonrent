from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Room
from ror.forms import FeedbackForm, RoomForm


# Create your views here.

@login_required(login_url='/ror/login/')
def index(request):

    rooms = Room.objects.all()

    return render(request,'index.html', {'rooms':rooms})

def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect('/ror/index/')
        else:
            messages.add_message(request, messages.ERROR, "Incorrect username or password!")
    else:
        try:
            if request.user.is_authenticated:
                return redirect('/ror/index/')
        except Exception as e:
            messages.add_message(request, messages.ERROR, str(e))
    return render(request,'log_in.html')

@login_required(login_url='/ror/login/')
def log_out(request):
    logout(request)
    return redirect('/ror/login/')

def sign_up(request):
    if request.user.is_authenticated:
            return redirect('/ror/index/')

    if request.method == "POST":
        user = User()
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.password = make_password(request.POST.get('password'))
        user.save()
        # if user:
        #     login(request, user)
        #     return redirect('/vault/index/')
        messages.add_message(request, messages.SUCCESS, "Account created successfully, sign in to continue!")
        return redirect('/ror/login/')
    # else:
    #     try:
    #         if request.user.is_authenticated:
    #             return redirect('/vault/index')
    #     except Exception as e:
    #         print(e)

    return render(request,'sign_up.html')

@login_required(login_url="/ror/login/")
def feedback(request):

    form = FeedbackForm()

    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect("/ror/index/")

    return render(request, 'feedback.html', {'form': form})


@login_required(login_url="/ror/login/")
def add_room(request):

    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect("/ror/index/")

    return render(request, 'add_room.html', {'form': form})

