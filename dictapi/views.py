from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .util import get_word_meaning

@api_view(['GET'])
def dict_list(request):
    query = request.GET.get('query')

    if query is None:
        return Response(data={'query': 'required'}, status=status.HTTP_400_BAD_REQUEST)

    result = get_word_meaning(query)
    if result is not None:
        return Response(data={'word': query, 'definitions': result}, status=status.HTTP_200_OK)
    return Response(data={'error': 'could not find word'}, status=status.HTTP_404_NOT_FOUND)

    

