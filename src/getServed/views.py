from django.shortcuts import render

# Create your views here.
def home(request):

	return render(request, "home.html", {})
	
def searchResult(request):

	return render(request, "searchResult.html", {})
	
def loginPage(request):

	return render(request, "loginPage.html", {})