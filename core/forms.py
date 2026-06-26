from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile


class RegistroForm(UserCreationForm):
    """Formulario de registro con validación de email obligatorio y único."""

    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe una cuenta con este correo electrónico.")
        return email

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            Profile.objects.get_or_create(user=user)
        return user


class PostForm(forms.ModelForm):
    """Formulario para crear y editar entradas, con validación mínima de contenido."""

    class Meta:
        model = Post
        fields = ["title", "content", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título de la entrada"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 8, "placeholder": "Escribí el contenido aquí..."}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if len(title) < 5:
            raise forms.ValidationError("El título debe tener al menos 5 caracteres.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get("content", "").strip()
        if len(content) < 20:
            raise forms.ValidationError("El contenido debe tener al menos 20 caracteres.")
        return content


class ProfileForm(forms.ModelForm):
    """Formulario para editar el perfil del usuario."""

    class Meta:
        model = Profile
        fields = ["bio", "avatar"]
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Contanos sobre vos..."}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
