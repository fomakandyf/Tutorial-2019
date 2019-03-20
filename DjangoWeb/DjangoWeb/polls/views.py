
from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'polls/index.html',
        {
            'title':'Polls Page',
            'content':"Welcome to the polls application",
        }
    )

def detail(request, question_id):
    return HttpRequest("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking as the results of question %s"
    return HttpRequest( response % question_id)

def vote(request, question_id):
    return HttpRequest("You aew voting on question %s" % question_id)
