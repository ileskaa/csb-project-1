from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def indexview(request):
    return render(
        request,
        "index.html",
        {
            "visibility": "hidden"
        }
    )


def register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, password=password)
    print('Created user', user)
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect
    return HttpResponseRedirect("/brokenapp/")


def signin(request):
    if not request.POST:
        return render(
            request,
            "index.html",
            {"visibility": "visible"}
        )
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        print('user', user, 'is now authenticated')
        return HttpResponseRedirect("/brokenapp/")
    else:
        print('Failed to authenticate')
        # This must be fixed
        return render(
            request,
            "index.html",
            {
                "error_message": "Wrong username or password",
                "visibility": "visible"
            }
        )
