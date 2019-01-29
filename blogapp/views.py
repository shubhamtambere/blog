from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Article
# Create your views here.
def home_view(*args, **kwargs):
    return(HttpResponse('Home page'))

def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogapp/article_list.html', {'articles':articles})
