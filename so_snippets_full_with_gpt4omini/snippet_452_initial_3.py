class Mock:# pragma: no cover
    def filter(self, func): pass# pragma: no cover
# pragma: no cover
register = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1118183/how-to-debug-in-django-the-good-way
from l3.Runtime import _l_
@register.filter 
def pdb(element):
    _l_(1604)

    try:
        import pdb; 
        _l_(1602)

    except ImportError:
        pass
    aux = element
    _l_(1603)
    return aux

