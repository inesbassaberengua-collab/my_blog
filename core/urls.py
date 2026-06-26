from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post_list, name="post_list"),
    path("posts/nuevo/", views.post_create, name="post_create"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("posts/<int:pk>/editar/", views.post_edit, name="post_edit"),
    path("posts/<int:pk>/eliminar/", views.post_delete, name="post_delete"),
    path("registro/", views.registro, name="registro"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("perfil/", views.perfil, name="perfil"),
]
