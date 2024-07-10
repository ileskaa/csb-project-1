"""
URL configuration for csbproject1 project.

The urlpatterns-list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.testview, name="test"),
    # include() allows referencing other URLconfs
    path("brokenapp/", include("brokenapp.urls")),
    # path() is passed 4 args. 2 required: route and view;
    # 2 optional: kwargs and name.
    # view: when django finds a matching pattern, it calls the specified
    # view function with an HttpRequest object as the 1st arg and
    # any captured values from the route as kwargs.
    # kwargs: arbitrary keyword args can be passed in ad dictionary
    # to the target view.
    # name: naming the URL lets you refer to it unambiguously
    # from elsewhere in your DJango project
    path('admin/', admin.site.urls),
]
