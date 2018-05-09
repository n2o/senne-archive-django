from django import template

register = template.Library()


@register.filter(is_safe=True)
def html_paragraph_if_field_exists(field, name):
    if field:
        return "<p>{}: {}</p>".format(name, field)
    return ""
