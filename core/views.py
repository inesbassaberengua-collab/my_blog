from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Post, Profile
from .forms import RegistroForm, PostForm, ProfileForm


def home(request):
    """Página de inicio pública con las últimas entradas."""
    posts = Post.objects.all()[:5]
    return render(request, "home.html", {"posts": posts})


def post_list(request):
    """Listado completo de entradas, con búsqueda opcional por autor o título."""
    query = request.GET.get("q", "")
    posts = Post.objects.all()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(author__username__icontains=query)
        )
    return render(request, "blog/post_list.html", {"posts": posts, "query": query})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "¡Entrada publicada correctamente!")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form, "titulo": "Nueva entrada"})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Entrada actualizada correctamente.")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form, "titulo": "Editar entrada"})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Entrada eliminada.")
        return redirect("post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "¡Cuenta creada con éxito! Bienvenido/a.")
            return redirect("home")
    else:
        form = RegistroForm()
    return render(request, "registration/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "registration/login.html"


@login_required
def perfil(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect("perfil")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "registration/profile.html", {"form": form})
