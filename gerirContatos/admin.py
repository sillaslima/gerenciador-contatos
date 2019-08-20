from django.contrib import admin

# Register your models here.
from gerirContatos.models import CanalContato,Contato
admin.site.register(Contato)
admin.site.register(CanalContato)
