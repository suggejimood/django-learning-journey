from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthChallenges = {
    "january": "Learn Python",
    "february": "Walk 20 min",
    "march": "Learn Django",
    "april": "Eat health food",
    "may": "Run 5 km",
    "june": "Learn English",
    "july": "Learn C++",
    "agust": "Learn TypeScript",
    "september": "Watch good movies",
    "october": "Fix broken cars",
    "novmeber": "Read new books",
    "december": None
}

def index(request):
    months = list(monthChallenges.keys())

    return render(request, "challenges/index.html", {"months": months})

def monthlyChallenge(request, month):
    try:
        challenge = monthChallenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge, "month": month})
    except:
        raise Http404()

def montlyChallengeNumber(request, month):
    months = list(monthChallenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Month Not Found!!!!")

    redirect = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect])

    return HttpResponseRedirect(redirect_path)