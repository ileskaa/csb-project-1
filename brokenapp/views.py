from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Choice, Question


# All views are responsible for doing one of two things:
# returning an HttpResponse object having the content of the requested page,
# or raising an exception such as Http404.

# Each genetric view needs to know what model it will be acting upon.
# This is provided either by defining the get_queryset() method
# or by using the model attribute.
# Generic views documentation:
# https://docs.djangoproject.com/en/5.0/topics/class-based-views/

class IndexView(generic.ListView):
    template_name = "brokenapp/index.html"
    # Provide context_object_name to override the automatically generated context variable
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions (excluding those set to be
        published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


def get_question(question_id):
    # Shortcut to replace try...except, get() and Http404.
    # Here we give it a Model and a lookup parameter as arguments
    question = get_object_or_404(Question, pk=question_id)
    return question


# Detailview is used to present extra information beyond that provided by the generic view
# https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/#adding-extra-context
class DetailView(generic.DetailView):
    model = Question
    # Tell django to use this name instead of autogenerated default
    template_name = "brokenapp/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "brokenapp/results.html"


# Remove the next line to block CSRF
@csrf_exempt
# urls.py sends a keyword argument called question_id to this view
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dict-like object that lets you access submitted data by key name
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "brokenapp/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # Instruct database to inc. vote count by 1
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("brokenapp:results", args=(question.id,)))
        # The reverse() function above helps avoid having to harcode a URL in the view func.
        # It is given the name of the view that we want to pass control to and
        # the variable portion of the URL pattern that points to that view.
        # So reverse() will return a string.


def injection(request):
    return render(request, "brokenapp/form.html")


def query(request):
    query = request.POST['query']
    # SELECT * FROM brokenapp_choice for ex.
    # SELECT * FROM brokenapp_choice
    print(query)
    try:
        result = []
        for c in Choice.objects.raw(query):
            print(c)
            result.append(c)
        # return HttpResponseRedirect(reverse("brokenapp:injection"))
        return render(
            request,
            "brokenapp/form.html",
            {
                "result": result
            }
        )
    except TypeError:
        return render(
            request,
            "brokenapp/form.html",
        )
