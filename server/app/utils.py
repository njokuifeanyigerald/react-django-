from re import I
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def getNoteList(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)


body_param = openapi.Parameter('body', in_=openapi.IN_QUERY, description='desciption', type=openapi.TYPE_STRING)
@swagger_auto_schema(manual_parameters=[body_param])
def createNote(request):
    data = request.data
    body =  data['body']
    notes = Note.objects.create(
        body= body
    )
    serializer = NoteSerializer(notes, many=False)

    return Response(serializer.data)

def getNoteDetail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)

def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note successfully deleted')