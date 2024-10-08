from django.urls import path

from . import views

# Namespacing
app_name = "brokenapp"
urlpatterns = [
    # as_view() is required for class-based views
    path("", views.IndexView.as_view(), name="index"),
    # angle brackets are used to capture part of the URL
    # and send it as a keyword arg to the view
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("injection/", views.injection, name="injection"),
    # INJECTION DANGER:
    path("query/", views.query, name="query"),
]
