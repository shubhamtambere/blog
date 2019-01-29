from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(*args, **kwargs):
    return(HttpResponse('Home page'))

def article_list(request):
    return render(request, 'blogapp/article_list.html', {})
