from PIL import Image # pragma: no cover

PIL = type('Mock', (object,), {'Image': Image})() # pragma: no cover

from PIL import Image # pragma: no cover
import requests # pragma: no cover
from io import BytesIO # pragma: no cover

requests.get = lambda url, **kwargs: type('MockResponse', (object,), {'content': b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x90\x00\x00\x00\xc8\x08\x06\x00\x00\x00\x7e\xd6!\x90\x00\x00\x00\x13IDATx\x9c\xed\xc1\x01\x0c\x00\x00\x00\x82 A\x8f\xe5Q\xed\x00\x00\x00\x00IEND\xa9B`\x82'}) # pragma: no cover
requests.get('http://lorempixel.com/400/200') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
from l3.Runtime import _l_
try:
    import io
    _l_(3340)

except ImportError:
    pass
try:
    import requests
    _l_(3342)

except ImportError:
    pass

r = requests.get('http://lorempixel.com/400/200')
_l_(3343)
r.raise_for_status()
_l_(3344)
with io.BytesIO(r.content) as f:
    _l_(3347)

    with Image.open(f) as img:
        _l_(3346)

        img.show()
        _l_(3345)
try:
    import requests
    _l_(3349)

except ImportError:
    pass

r = requests.get('http://lorempixel.com/400/200', stream=True)
_l_(3350)
r.raise_for_status()
_l_(3351)
r.raw.decode_content = True  # Required to decompress gzip/deflate compressed responses.
_l_(3352)  # Required to decompress gzip/deflate compressed responses.
with PIL.Image.open(r.raw) as img:
    _l_(3354)

    img.show()
    _l_(3353)
r.close()  # Safety when stream=True ensure the connection is released.
_l_(3355)  # Safety when stream=True ensure the connection is released.

