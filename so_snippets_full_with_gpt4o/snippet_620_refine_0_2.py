from PIL import Image # pragma: no cover
import PIL # pragma: no cover

Image = PIL.Image # pragma: no cover
PIL.Image = PIL.Image # pragma: no cover

from PIL import Image # pragma: no cover
from PIL import UnidentifiedImageError # pragma: no cover
import PIL # pragma: no cover

Image = PIL.Image # pragma: no cover
PIL.Image = PIL.Image # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
from l3.Runtime import _l_
try:
    import io
    _l_(13229)

except ImportError:
    pass
try:
    import requests
    _l_(13231)

except ImportError:
    pass

r = requests.get('http://lorempixel.com/400/200')
_l_(13232)
r.raise_for_status()
_l_(13233)
with io.BytesIO(r.content) as f:
    _l_(13236)

    with Image.open(f) as img:
        _l_(13235)

        img.show()
        _l_(13234)
try:
    import requests
    _l_(13238)

except ImportError:
    pass

r = requests.get('http://lorempixel.com/400/200', stream=True)
_l_(13239)
r.raise_for_status()
_l_(13240)
r.raw.decode_content = True  # Required to decompress gzip/deflate compressed responses.
_l_(13241)  # Required to decompress gzip/deflate compressed responses.
with PIL.Image.open(r.raw) as img:
    _l_(13243)

    img.show()
    _l_(13242)
r.close()  # Safety when stream=True ensure the connection is released.
_l_(13244)  # Safety when stream=True ensure the connection is released.

