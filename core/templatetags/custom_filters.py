from django import template

register = template.Library()


@register.filter(name="resumen")
def resumen(value, palabras=20):
    """Devuelve las primeras N palabras de un texto, seguidas de '...' si se corta."""
    if not value:
        return ""
    lista = value.split()
    if len(lista) <= int(palabras):
        return value
    return " ".join(lista[: int(palabras)]) + "..."
