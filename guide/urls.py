"""guide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from blog.views import ArticleDeleteView, ArticleListView, ArticleDetailView , ArticleCreateView , ArticleUpdateView
from accounts.views import UserFormView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('blog/<int:id>/update/' , ArticleUpdateView.as_view()),
    path('blog/create/',ArticleCreateView.as_view()),
    path('blog/<int:id>/',ArticleDetailView.as_view(),name=  'article-detail'),
    path('blog/',ArticleListView.as_view(),name= 'article-list'),
    path('admin/', admin.site.urls),
    path('home/',views.main, name = "main"),
    path('search/',views.search,name= "search"),
    path('register/',views.register),
    path('<int:id>/detail/',views.detail),
    path('blog/', include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path('login/',UserFormView.as_view()),
    path('arts/',include('arts.urls')),
     
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
