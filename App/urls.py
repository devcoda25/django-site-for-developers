from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('room/<int:room_id>/', views.item_detail, name='room_detail'),
    path('updateroom/<int:room_id>/update/', views.update_room, name='update_room'),
    path('deleteroom/<int:room_id>/delete/', views.delete_room, name='delete_room'),
    path('conform/<int:room_id>/conform/', views.confirm_delete_room, name='confirm_delete_room'),
    path('search/', views.search_results, name='search_results'),

    path('create_room/', views.create_room, name='create_room'),
]


