from django import template
# Crea un decorar que va a permitir utilizar el filtro
register = template.Library()

# registrar un filtro 
# agregar el nombre del filtro que es (name="add_attr")
@register.filter(name="add_attr")
# Crear la funcion tambien con  el nombre de add_attr
# recibe el field y el atributo que seria la clase que es is-invalid
# este attrs es el atributo que esta en input.html que es {{ widget.attrs.class }}
def add_attr(field, css):
    # Crear un diccionario 
    attrs = {}
    # Este split es por "class:is-invalid" que esta en form_snippet
    clase, valor = css.split(':')
    attrs[clase] = valor
    return field.as_widget(attrs=attrs)


