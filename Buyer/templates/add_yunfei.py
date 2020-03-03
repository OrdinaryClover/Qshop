from django import template
register = template.Library()

@register.filter()



def add_yun(num):
    yunfei = 10
    return num + yunfei
