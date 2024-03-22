from django.db import models


# Create your models here.
class Student(models.Model):
  matricula = models.PositiveIntegerField()
  nome = models.CharField(max_length=50)
  sobrenome = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  curso = models.CharField(max_length=50)
  media = models.FloatField()

  def __str__(self):
    return f'Student: {self.nome} {self.sobrenome}'
