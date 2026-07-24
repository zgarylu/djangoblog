from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'appname/index.html')
@login_required
def secret(request):
    return render(request, 'appname/secret.html')
