markdown
# Despliegue en Render

Este proyecto está preparado para desplegarse en Render como un Web Service gratuito.

## Variables de entorno necesarias en Render

| Variable | Valor |
|---|---|
| SECRET_KEY | una clave secreta generada |
| RENDER | true |
| RENDER_EXTERNAL_HOSTNAME | la completa Render automáticamente |
| DATABASE_URL | la completa Render automáticamente |

## Comando de build
bash build.sh

## Comando de start
gunicorn config.wsgi:application

## Librerías agregadas para producción
- gunicorn: servidor WSGI de producción.
- whitenoise: sirve archivos estáticos.
- dj-database-url: usa DATABASE_URL de Render.
- psycopg2-binary: driver PostgreSQL.
