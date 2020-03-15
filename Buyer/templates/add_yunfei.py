from django import template
register = template.Library()

@register.filter()
def add_yun(num):
    yunfei = 10
    return num + yunfei

@register.filter
def mobile_hidden(mobile):
    if mobile and len(mobile) >= 7:
        md = mobile[3:7]
        mobile = mobile.replace(md, '****')
    return mobile
