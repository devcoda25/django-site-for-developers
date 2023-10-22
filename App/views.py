
from django.shortcuts import render, get_object_or_404,redirect
from .forms import RoomForm
from .models import *

def index(request):
    return render(request, 'index.html')

def item_detail(request, room_id):
    roomdetails = get_object_or_404(Room, id=room_id)
    return render(request, 'roomdetails.html', {'roomdetails': roomdetails})

def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page or another URL
    else:
        form = RoomForm()
    
    return render(request, 'roomform.html', {'form': form})

def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_detail', room_id=room_id)
    else:
        form = RoomForm(instance=room)

    return render(request, 'updateroom.html', {'form': form, 'room': room})

 

def confirm_delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'deleteroom.html', {'room': room})

def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    return redirect('index')

def search_results(request):
    query = request.GET.get('query')
    rooms = Room.objects.filter(topic__name__icontains=query)
    return render(request, 'search_results.html', {'query': query, 'rooms': rooms})