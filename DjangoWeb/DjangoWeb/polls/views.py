
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
