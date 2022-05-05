from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('consent/', views.ConsentCreateView.as_view(), name='consent_form'),
    path('njform/', views.njconsentview.as_view(), name='nj_consent_form'),
    path('consent/success', views.success, name='success'),
]