"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blank),
    path('index.html', views.blank),
    path('DM_page.html', views.friend),
    path('Login.html', views.login),
    path('Register.html', views.register),
    path('admin/', admin.site.urls),
    path("file-upload", views.upload),
    path("word-upload", views.message),
    path("comment-path", views.comment),
    path("like-path", views.like),
    path("textlike-path", views.textlikes),
    path("textcomment-path", views.textcomment),
    path('files-upload', views.files),
    path("filecomment-path", views.filec),
    path("filelike-path", views.filel),
    # websocket
    #path('templates/chat/index.html', views.chat)

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
