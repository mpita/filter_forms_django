from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Usuerio"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.TextField(verbose_name="Pregunta")

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="Pregunta"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(verbose_name="Respuesta")

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"

    def __str__(self):
        return self.question.__str__()