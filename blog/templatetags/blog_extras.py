from django import template
register = template.Library()
from django.contrib.auth import get_user_model
user_model = get_user_model()
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe


@register.filter
def author_details(author):
    if not isinstance(author, user_model):
        return ""

    if author.first_name and author.last_name:
        name = escape(f"{author.first_name} {author.last_name}")
    else:
        name = escape(f"{author.username}")

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html('</a>')
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)

@register.simple_tag
def endcol(extra_classes=""):
    return format_html('</div>')

@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
    return format_html("</div>")