from .models import *

def get_rooms(request):
    rooms = Room.objects.all()
    return {'rooms': rooms}

def topics_and_room_counts(request):
    topics = Topic.objects.all()
    topic_counts = {}

    for topic in topics:
        room_count = Room.objects.filter(topic=topic).count()
        topic_counts[topic] = room_count

    return {'topics_and_room_counts': topic_counts}
