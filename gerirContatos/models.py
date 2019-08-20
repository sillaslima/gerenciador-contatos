from django.db import models

# Create your models here.

class CanalContato (models.Model):
    canal = models.CharField(max_length=12, blank=False, null=False)

    def __str__(self):
        return self.canal


class Contato(models.Model):
    nome = models.CharField(max_length=156, blank=False, null=False)
    canal = models.ForeignKey ( CanalContato , on_delete=False , blank=True , null=True , default='TBD' )
    valor = models.CharField(max_length=156, blank=False, null=False)
    obs = models.CharField(max_length=156, blank=True, null=True)

    def __str__(self):
        return self.nome



