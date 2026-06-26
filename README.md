# 📝 Mi Blog Django — Proyecto Final

Aplicación web desarrollada con **Django** como proyecto final del curso de Python. El objetivo del proyecto es implementar una aplicación web completa que permita la gestión de publicaciones de un blog, aplicando los conceptos fundamentales del framework Django, el uso de bases de datos, autenticación de usuarios y despliegue en la nube.

---

## 📖 Descripción

Esta aplicación permite que los usuarios puedan registrarse, iniciar sesión y administrar publicaciones de un blog de manera sencilla e intuitiva.

Cada usuario autenticado puede crear, editar y eliminar sus propias entradas, mientras que cualquier visitante puede navegar por el contenido publicado. Además, el sistema cuenta con perfiles de usuario, carga opcional de imágenes, búsqueda de publicaciones y un panel de administración para gestionar toda la información del sitio.

El proyecto fue desarrollado utilizando buenas prácticas de programación y la arquitectura Modelo-Vista-Template (MVT) propia de Django.

---

## ✨ Funcionalidades principales

* 🔐 Registro de nuevos usuarios.
* 👤 Inicio y cierre de sesión.
* 📝 Creación de publicaciones con título, contenido e imagen opcional.
* ✏️ Edición de publicaciones únicamente por su autor.
* 🗑️ Eliminación de publicaciones.
* 🔎 Búsqueda de entradas por diferentes criterios.
* 👥 Perfil de usuario editable.
* 🖼️ Gestión de imágenes mediante Django.
* ⚙️ Panel de administración de Django (`/admin/`).
* ✔️ Formularios con validación de datos.
* 💾 Base de datos administrada mediante Django ORM.

---

## 🛠️ Tecnologías utilizadas

* Python 3
* Django
* HTML5
* CSS3
* Bootstrap
* SQLite (desarrollo)
* PostgreSQL (producción en Render)
* WhiteNoise
* Gunicorn

---

## 💻 Instalación local (Windows)

1. Clonar el repositorio:

```powershell
git clone https://github.com/TU_USUARIO/mi-blog-django.git
```

2. Ingresar al proyecto:

```powershell
cd mi-blog-django
```

3. Crear un entorno virtual:

```powershell
python -m venv venv
```

4. Activar el entorno virtual:

```powershell
venv\Scripts\activate
```

5. Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

6. Aplicar las migraciones:

```powershell
python manage.py migrate
```

7. Crear un superusuario:

```powershell
python manage.py createsuperuser
```

8. Ejecutar el servidor de desarrollo:

```powershell
python manage.py runserver
```

Luego abrir el navegador en:

```text
http://127.0.0.1:8000/
```
##👤 Autores

Búsqueda de autores por nombre
Visualización de datos básicos (nombre y email)

##🔐 Autenticación

Registro de usuarios
Login de usuarios
Logout seguro

##🧠 Panel de administración

Gestión completa desde Django Admin
---

## ☁️ Despliegue

El proyecto está preparado para desplegarse en **Render** utilizando **Gunicorn**, **WhiteNoise** y **PostgreSQL**.

La configuración necesaria para el despliegue se encuentra documentada en:

```text
docs/deploy.md
```

---

## 📂 Estructura principal del proyecto

```text
Proyecto
│
├── blog/
├── config/
├── core/
├── docs/
├── media/
├── static/
├── users/
├── manage.py
├── requirements.txt
├── Procfile
├── build.sh
└── README.md
```
##🎯 Conceptos aplicados

Modelos con relaciones (ForeignKey / ManyToMany)
Validaciones personalizadas (clean())
Class Based Views (ListView, DetailView, CreateView, UpdateView, DeleteView)
Templates con herencia
Context processors
Template tags y filtros personalizados
URLs con namespacing
Formularios Django con validación
Seguridad CSRF
Django Admin
---

## 🚀 Autor

Proyecto desarrollado como trabajo final del curso de Python con Django.

**Autor:** Ines Bassa

---

## 📌 Estado del proyecto

✅ Proyecto finalizado y preparado para su despliegue en Render.
