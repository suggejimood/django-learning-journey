from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Run in the forest"
}

def index(request):
    listItems = ""
    months = list(monthChallenges.keys())

    for month in months:
        capitilazedMonth = month.capitalize()
        monthPath = reverse("month-challenge", args=[month])
        listItems += f"<li> <a href=\"{monthPath}\">{capitilazedMonth}</a> </li>"

    responseData = f"""
    <h1>Months</h1>
    <ul> {listItems} </ul>
    """
    
    return HttpResponse(responseData)

def monthlyChallenge(request, month):
    try:
        challenge = monthChallenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge, "month": month.capitalize()})
    except:
        return HttpResponseNotFound("Month not found")

def montlyChallengeNumber(request, month):
    months = list(monthChallenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Month Not Found!!!!")

    redirect = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect])

    return HttpResponseRedirect(redirect_path)