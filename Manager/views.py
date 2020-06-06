from django.shortcuts import render
from django.http import HttpResponse
from .models import Bookmark


#links
def home(request):
	return render(request, "Manager/home.html", {"BM" : Bookmark.objects.all()})
