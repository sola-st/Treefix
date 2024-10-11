from PIL import Image # pragma: no cover
import requests # pragma: no cover

Image = type('MockImage', (object,), {'open': staticmethod(lambda f: f)}) # pragma: no cover
PIL = type('MockPIL', (object,), {'Image': Image}) # pragma: no cover

from PIL import Image # pragma: no cover
import requests # pragma: no cover

Image = type('MockImage', (object,), {'open': staticmethod(lambda f: f)}) # pragma: no cover
PIL = type('MockPIL', (object,), {'Image': Image}) # pragma: no cover
requests.get = lambda url, stream=False: type('MockResponse', (object,), {'status_code': 200, 'content': b'', 'raw': type('MockRaw', (object,), {'decode_content': False})(), 'raise_for_status': lambda self: None})() if url == 'http://example.com' else type('MockResponse', (object,), {'status_code': 429, 'content': b'', 'raw': None, 'raise_for_status': lambda self: (_ for _ in ()).throw(requests.exceptions.HTTPError('429 Client Error: Too Many Requests'))})() # pragma: no cover

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

