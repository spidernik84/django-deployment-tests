from django import template

register = template.Library()

# def cut(value,arg):
#     """
#     Cuts out all values of "arg" from the string
#     """
#     return value.replace(arg,'')

# register.filter('cut',cut)


# same as above but with decorator!
@register.filter(name='cut')
def cut(value, arg):
    """
    Cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')
