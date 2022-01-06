from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_data/', views.save_data, name='save_data'),
    path('updated_data/', views.updated_data, name='updated_data'),
    path('delete_data/', views.delete_data, name='delete_data'),
]
