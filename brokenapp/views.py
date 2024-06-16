from django.shortcuts import get_object_or_404, render

from .models import Question


# Create your views here.
# All views are responsible for doing one of two things:
# returning an HttpResponse object having the content of the requested page,
# or raising an exception such as Http404.
def index(request):
    # display the latest 5 poll questions in the system, separated by commas,
    # according to publication date
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    # The context is a dictionary that maps template variable names
    # to Python objects.
    # render() is a shortcut that replaces loader.get_template() and HttpResponse().
    # It returns an HttpResponse object of the given template rendered with the given context.
    return render(request, "brokenapp/index.html", context)


def get_question(question_id):
    # Shortcut to replace try...except, get() and Http404.
    # Here we give it a Model and a lookup parameter as arguments
    question = get_object_or_404(Question, pk=question_id)
    return question


# The following views are different from the previous since they take an arg
def detail(request, question_id):
    question = get_question(question_id)
    context = {"question": question}
    return render(request, "brokenapp/detail.html", context)


def results(request, question_id):
    question = get_question(question_id)
    return render(request, "brokenapp/results.html", {"question": question})


def vote(request, question_id):
    question = get_question(question_id)
    return render(request, "brokenapp/vote.html", {"question": question})
