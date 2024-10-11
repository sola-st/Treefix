from PIL import Image # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6444548/how-do-i-get-the-picture-size-with-pil
from l3.Runtime import _l_
try:
    from PIL import Image
    _l_(2039)

except ImportError:
    pass

im = Image.open('whatever.png')
_l_(2040)
width, height = im.size
_l_(2041)

