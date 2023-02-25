from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def event(request,pk):
    event = Event.objects.filter(id=pk)
    serializer = EventSerializer(event,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user(request,pk):
    user = User.objects.filter(id=pk)
    serializer = UserSerializer(user,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def calendars(request):
    calendars = Calendar.objects.all()
    serializer = UserSerializer(calendars,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def calendar(request,pk):
    calendar = Calendar.objects.filter(id=pk)
    serializer = CalendarSerializer(calendar,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def invites(request):
    invites = Invites.objects.all()
    serializer = InvitesSerializer(invites,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def invite(request,pk):
    invite = Invites.objects.filter(id=pk)
    serializer = InvitesSerializer(invite,many=True)
    return Response(serializer.data)