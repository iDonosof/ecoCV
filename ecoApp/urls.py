from django.urls import path
from . import views
from django.conf.urls import include,url
from qr_code import urls as qr_code_urls

urlpatterns = [
    path('', views.event_information, name='event_information'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('personal_information/', views.personal_information, name='personal_information'),
    path('personal_curriculum/', views.personal_curriculum, name='personal_curriculum'),
    path(r'^qr_code/', include(qr_code_urls, namespace = "qr_cde")),
]
