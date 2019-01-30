from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('about', views.about, name='about'),
    re_path(r'^article/(?P<article_id>\d+)/$', views.article_detail, name='detail_view'),
]
