from django.urls import path
from . import views

urlpatterns = [
    path('', views.available_items, name='available_items'),
    path('sponsor/<int:item_id>/<int:institution_id>/', views.sponsor_item, name='sponsor_item'),
    path('chat/<int:institution_id>/', views.chat_with_institution, name='chat_with_institution'),
]
