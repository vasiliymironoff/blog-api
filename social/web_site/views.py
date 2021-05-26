from django.shortcuts import render


def index(request):
    return render(request, "web_site/index.html")
