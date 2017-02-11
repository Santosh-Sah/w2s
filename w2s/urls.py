from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views
from login.models import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('login.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),  
]    