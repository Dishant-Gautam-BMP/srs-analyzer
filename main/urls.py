from django.urls import path
from main import views

urlpatterns = [
    path('', views.root, name="root"),
    path('index', views.index, name='index'),
    path('input', views.input, name='input'),
    path('analyze_reqs', views.analyze_reqs, name='analyze_reqs')
]