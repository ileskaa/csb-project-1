from django.urls import path

from . import views

# Add a namespace
app_name = "brokenapp"
urlpatterns = [
    # as_view() is required for class-based views
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
