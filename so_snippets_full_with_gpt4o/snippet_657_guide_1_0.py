requests = type('Mock', (object,), {'get': lambda url: type('Mock', (object,), {'content': b''})()}) # pragma: no cover
Image = type('Mock', (object,), {'value': b''}).value # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/32370281/how-to-embed-image-or-picture-in-jupyter-notebook-either-from-a-local-machine-o
from l3.Runtime import _l_
try:
    import requests
    _l_(15031)

except ImportError:
    pass
try:
    from ipywidgets import Image
    _l_(15033)

except ImportError:
    pass

Image(value=requests.get('https://octodex.github.com/images/yaktocat.png').content)
_l_(15034)

