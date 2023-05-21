from django.shortcuts import render, redirect

def index(request):
    message = ""
    if request.method == "POST":
        if request.POST.get("password","") == "123":
            return redirect("/house")
        else:
            message = "Incorrect password"
    context = {"message": message}
    return render(request, "plebzz.html", context)

def house(request):
    return render(request, "plebzz2.html")