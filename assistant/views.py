from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def suggesions(request):
    # print(request.headers.get('name'))
    sentence = {'sentence': 'This is a test sentence. so speak loudly, Thank you'}
    return Response(sentence)
