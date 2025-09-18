from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Crear el modelo de Tarea
class Tarea(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    datecomplete = models.DateTimeField(null=True,)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# Representacion en string del modelo
    def __str__(self):
        return f"{self.title} - {self.user.username if self.user else 'No User'}"
