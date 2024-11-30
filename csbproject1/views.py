from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def indexview(request):
    return render(
        request,
        "auth.html",
        {"visibility": "hidden", "action_path": "/signin/", "form_title": "Sign in"},
    )


def render_registration_page(request, error = ""):
    return render(
        request,
        "auth.html",
        {
            "visibility": "visible",
            "action_path": "/register/",
            "form_title": "Register",
            "error_message": error
        },
    )


def check_validity(password):
    if len(password) < 8:
        return False

    lower = upper = digit = False

    for character in password:
        if character.islower():
            lower = True

        if character.isupper():
            upper = True

        if character.isdigit():
            digit = True

    if lower and upper and digit:
        return True

INVALID_PSWD = "The password must contain at lest 8 characters, " \
    "including uppercase and lowercase letters, and digits"

def register(request):
    if not request.POST:
        return render_registration_page(request)
    username = request.POST["username"]
    password = request.POST["password"]
    # FLAW 1: uncomment the 3 lines below to enforce pswd requirements
    # is_valid = check_validity(password)
    # if not is_valid:
    #     return render_registration_page(request, INVALID_PSWD)
    user = User.objects.create_user(username, password=password)
    request.session["username"] = username
    print("Created user", user)
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect
    return HttpResponseRedirect("/brokenapp/")


def render_signin(request):
    return render(
        request,
        "auth.html",
        {"visibility": "visible", "action_path": "/signin/", "form_title": "Sign in"},
    )


# I should actually move this /brokenapp
def signin(request):
    if not request.POST:
        return render_signin(request)
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        request.session["username"] = username
        print("user", user, "is now authenticated")
        return HttpResponseRedirect("/brokenapp/")
    print("Failed to authenticate")
    # This must be fixed
    return render(
        request,
        "auth.html",
        {
            "error_message": "Wrong username or password",
            "visibility": "visible",
            "action_path": "/signin/",
            "form_title": "Sign in",
        },
    )


def logout(request):
    request.session.clear()
    return HttpResponseRedirect("/signin/")
