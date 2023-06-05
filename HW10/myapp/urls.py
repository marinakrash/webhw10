from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('detail/<int:quote_id>', views.detail, name='detail'),
]