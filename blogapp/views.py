from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Article
from .models import Author
# Create your views here.
def home_view(*args, **kwargs):
    return(HttpResponse('Home page'))

def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogapp/article_list.html', {'articles':articles})

def about(request):
    about_me = Author.objects.all()[:1].get()
    return render(request, 'blogapp/about.html', {'about_me': about_me})

def article_detail(request, article_id):
    detail = Article.objects.get(id=article_id)
    print(detail.content)
    return render(request, 'blogapp/article.html', {'detail': detail})
