"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from api.views import get_mood_view, get_movie_view, get_emotion_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/get_mood/', view=get_mood_view, name='get_mood'),
    path('api/v1/get_emotion/', view=get_emotion_view, name='get_emotion'),
    path('api/v1/get_movie/', view=get_movie_view, name='get_movie'),
]
