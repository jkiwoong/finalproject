from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from my_login.forms import RegisterForm
# Create your views here.

@csrf_exempt
def index(request):
    if request.user.is_authenticated is False:
        user = "Anonymous User!"
    else:
        user = User.objects.filter(id=request.user.id).first()
    return render(request, "my_login/index.html", {"welcome_msg": f"Hello, {user}"})

@csrf_exempt
def resister(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        msg = "올바르지 않은 데이터 입니다."
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = "회원가입 완료"
            return redirect("index")
        return render(request, "my_login/register.html", {"form": form, "msg": msg})
    else:
        form = RegisterForm()
        return render(request, "my_login/register.html", {"form": form})

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        msg = "가입되어 있지 않거나 로그인 정보가 잘못 되었습니다."
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                msg = "로그인 성공"
                login(request, user)
                return redirect("index")
        return render(request, "my_login/login.html", {"form": form, "msg": msg})
    else:
        form = AuthenticationForm()
        return render(request, "my_login/login.html", {"form": form})

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect("index")

@csrf_exempt
def user_list(request):
    if request.user.is_authenticated is False:
        return redirect("login")
    else:
        page = int(request.GET.get("page", 1))
        users = User.objects.all().order_by("-id")
        paginator = Paginator(users, 3)
        users = paginator.get_page(page)
        return render(request, "my_login/user_list.html", {"users": users, "request": request})
