from rest_framework import serializers
from .models import CanalContato, Contato


class CanalContatoSerializer(serializers.ModelSerializer):
    class Meta:
        canal = CanalContato
        fields = ('id','canal')



class ContatoSerializer(serializers.ModelSerializer):
    canal = serializers.SlugRelatedField ( queryset=CanalContato.objects.all ( ) , slug_field='canal' )

    class Meta:
        model = Contato
        fields = ('id','nome', 'canal', 'valor', 'obs')
