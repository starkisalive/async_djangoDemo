"""async_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import home_view, main_view, main_view_async,scrape_view_sync, scrape_view_async

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('sync/', main_view, name = 'sync-main-view'),
    path('async/', main_view_async, name = 'async-main-view'),
    path('async_scrape/', scrape_view_async, name = 'async-scrape-view' ),
    path('sync_scrape/', scrape_view_sync, name = 'sync-scrape-view' ),
]
