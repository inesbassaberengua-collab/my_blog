from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    """Entrada de blog creada por un usuario registrado."""

    title = models.CharField("Título", max_length=200)
    content = models.TextField("Contenido")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", verbose_name="Autor"
    )
    image = models.ImageField(
        "Imagen", upload_to="posts/", blank=True, null=True
    )
    published_date = models.DateTimeField("Fecha de publicación", default=timezone.now)
    updated_date = models.DateTimeField("Última edición", auto_now=True)

    class Meta:
        ordering = ["-published_date"]
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return self.title


class Profile(models.Model):
    """Perfil extendido del usuario, creado automáticamente al registrarse."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField("Biografía", max_length=300, blank=True)
    avatar = models.ImageField("Avatar", upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

# Create your models here.
