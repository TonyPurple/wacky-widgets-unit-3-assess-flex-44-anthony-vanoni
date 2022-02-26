from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def index(request):
  return render(request, 'index.html')
