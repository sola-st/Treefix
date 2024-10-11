class Mock(object): pass # pragma: no cover
requests = Mock() # pragma: no cover
requests.get = Mock() # pragma: no cover
Image = Mock() # pragma: no cover
Image.return_value = 'Image object initialized' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/32370281/how-to-embed-image-or-picture-in-jupyter-notebook-either-from-a-local-machine-o
from l3.Runtime import _l_
try:
    import requests
    _l_(2845)

except ImportError:
    pass
try:
    from ipywidgets import Image
    _l_(2847)

except ImportError:
    pass

Image(value=requests.get('https://octodex.github.com/images/yaktocat.png').content)
_l_(2848)

