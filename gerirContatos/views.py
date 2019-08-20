from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import pagination
from rest_framework.reverse import reverse
from rest_framework.response import Response
from gerirContatos.models import Contato,CanalContato
from .serializers import CanalContatoSerializer,ContatoSerializer

class CanalContatoViewSet(generics.ListAPIView):
    queryset = CanalContato.objects.all()
    serializer_class = CanalContatoSerializer
    name='listar-canais'

class PaginacaoContato(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 0

class ContatosViewSet(generics.ListAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    pagination_class = PaginacaoContato
    name='listar'


class ContatoUpdateViewSet (generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    name='update'


class ContatoDetailViewSet (generics.RetrieveAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    name='detail'

class ContatoCreateViewSet (generics.CreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    name='create'


class ContatoDeleteViewSet ( generics.DestroyAPIView ):
    queryset = Contato.objects.all ( )
    serializer_class = ContatoSerializer
    name = 'delete'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({

            'listar': reverse(ContatosViewSet.name, request=request),
            })