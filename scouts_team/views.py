from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


scouts_team = {
"John": "scout",
"Jack": "swimmer",
"Bill": "hunter",
"Rob": "pathfinder"   
}


def index(request):
    context = {"scouts":scouts_team.keys()}
    return render(request, "informace\index.html", context)

def john(request):
    return render(request, "informace\john.html")

def jack(request):
    return render(request, "informace\jack.html")

def bill(request):
    return render(request, "informace\\bill.html")


def description(request, scout):
    description = scouts_team[scout]
    
    return render(request, "informace\description.html", {
        "scout": scout,
        "description":description
    })
