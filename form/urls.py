# from django.conf.urls import url
from django.conf.urls import url
from views import get_input
import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^form/$', login, {'template_name': 'form/form2.html'}),
    url(r'^input/$', views.get_input),
]
