from django.template.defaulttags import register # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1118183/how-to-debug-in-django-the-good-way
from l3.Runtime import _l_
@register.filter 
def pdb(element):
    _l_(13892)

    try:
        import pdb; 
        _l_(13890)

    except ImportError:
        pass
    aux = element
    _l_(13891)
    return aux

