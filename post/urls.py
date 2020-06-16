"""post URL Configuration

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
from user.views import home_view,create_post_view,all_post_view,latest_post,one_post

urlpatterns = [
	path('', home_view , name='home_view'),
	path('create/', create_post_view , name='create_post_view'),
	path('all_post/', all_post_view , name='all_post_view'),
	path('latest/', latest_post , name='latest_post'),
	path('<int>:id', one_post , name='one_post'),

    path('admin/', admin.site.urls),
]