"""exercise_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from exercise_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert', view=views.insert_data, name='insert'),
    path('bulk-insert', view=views.bulk_insert_data, name='bulk-insert'),
    path('bulk-update', view=views.bulk_update_data, name='bulk-update'),
    path('fetch-all', view=views.fetch_all, name='fetch-all'),
    path('cities-in-state', view=views.cities_in_state, name='cities-in-state'),
]
