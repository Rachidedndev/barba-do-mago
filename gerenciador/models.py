from django.db import models

class Lugar(models.Model):

  nome = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  gentilico = models.CharField(
    max_length=255,
    null=True,
    blank=True
  )

  apelido = models.CharField(
    max_length=255,
    null=True,
    blank=True
  )

  governante = models.CharField(
    max_length=255,
    null=True,
    blank=True
  )

  tamanho = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  descrição = models.TextField(
    default=0,
    null=True,
    blank=True
  )

  historia = models.TextField(
    default=0,
    null=True,
    blank=True
  )

  geografia = models.TextField(
    default=0,
    null=True,
    blank=True
  )

  defesas = models.TextField(
    default=0,
    null=True,
    blank=True
  )

  lei_e_ordem = models.TextField(
    default=0,
    null=True,
    blank=True
  )

  exportacoes = models.TextField(
    default=0,
    null=True,
    blank=True
  )

  importacoes = models.TextField(
    default=0,
    null=True,
    blank=True
  )

  cultura_e_Sociedade = models.TextField(
    default=0,
    null=True,
    blank=True
  )

  notas = models.TextField(
    default=0,
    null=True,
    blank=True
  )

def __str__(self):
        return self.nome


class NPC(models.Model):
  nome = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  especie = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  classe = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  antecedente = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  talentos = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  altura = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  peso = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  divindade = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  cidade_natal = models.ForeignKey(Lugar, on_delete=models.PROTECT, null=True, blank=True, related_name="npcs_nascidos_aqui")
  local_atual = models.ForeignKey(Lugar, on_delete=models.PROTECT, null=True, blank=True, related_name="npcs_presentes_aqui")

  def __str__(self):
    return self.nome
