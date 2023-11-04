"""arisen URL Configuration

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
from arisencode import views as arisen_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', arisen_views.home, name='home'),
    path('create/', arisen_views.create, name='create'),
    path('dashboard/', arisen_views.dashboard, name='dashboard'),
    path('addrecipe/', arisen_views.addrecipe, name='addrecipe'),
    path('editrecipe/<int:id>', arisen_views.editrecipe, name='editrecipe'),
    path('inactiverecipe/<int:id>', arisen_views.inactiverecipe, name='inactiverecipe'),
    path('inactiverecipeadmin/<int:id>', arisen_views.inactiverecipeadmin, name='inactiverecipeadmin'),
    path('saverecipe/', arisen_views.saverecipe, name='saverecipe'),
    path('admindb/', arisen_views.admindb, name='admindb'),
    path('logout/', arisen_views.logout, name='logout'),
]
