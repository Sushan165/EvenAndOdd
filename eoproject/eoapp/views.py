from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from random import * 

def pnf(request,exception):
	return redirect("home")

def ulogin(request):
	if request.user.is_authenticated:
		return redirect("uhome")
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username = un , password = pw)
		if usr is None:
			return render(request,"login.html", {"msg":"invalid Login"})
		else:
			login(request ,usr)
			return redirect("uhome")
	else:
		return render(request,"login.html")


def usignup(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    elif request.method == "POST":
        un = request.POST.get("un")
        try:
            user = User.objects.get(username=un)
            return render(request, "signup.html", {"msg": "Email already registered"})
        except User.DoesNotExist:
            text = "0123456789"
            pw = ""
            for i in range(4):
                r = randrange(len(text))
                pw = pw + text[r]
            print(pw)
            usr = User.objects.create_user(username=un, password=pw)
            usr.save()
            return render(request, "signup.html", {"msg": pw})  # Use the same template name "signup.html"
    else:
        return render(request, "signup.html")


def uhome(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			num = int(request.POST.get("num"))
			if num % 2 == 0:
				msg = "num " + str(num) + " is Even"
			else:
				msg = "num " +str(num) + " is Odd"
			return render(request,"home.html",{"msg":msg})
		else:
			return render(request,"home.html")
	else:
		return redirect("ulogin")

def ulogout(request):
	logout(request)
	return redirect("ulogin")

def usnp(request):
	return render(request,"snp.html")
