from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import getNoteDetail, getNoteList, createNote, updateNote,deleteNote

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    # safe means i can return more data than just a pythondictionary
    # return JsonResponse('Our API', safe=False)
    return Response(routes)

# body_param = openapi.Parameter('body', in_ =openapi.IN_QUERY, description='desciption', type=openapi.TYPE_STRING)

@api_view(['GET', 'POST'])
# @swagger_auto_schema(manual_parameters=[body_param])
def getNotes(request):
    if request.method == 'GET':
        return getNoteList(request)
    if request.method == 'POST':
        return createNote(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):
    if request.method == 'GET':
        return getNoteDetail(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)
    
    if request.method == 'DELETE':
        return deleteNote(request, pk)

