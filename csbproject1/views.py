from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def testview(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))


@csrf_exempt
def register(request):
    user = User.objects.create_user("james", password="johnpassword")
    print('created user', user)
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect
    return HttpResponseRedirect("/brokenapp/")
