import PIL.Image # pragma: no cover
import requests # pragma: no cover
import io # pragma: no cover

class MockResponse: # pragma: no cover
    def __init__(self, content): # pragma: no cover
        self.content = content # pragma: no cover
        self.raw = io.BytesIO(content) # pragma: no cover
        self.raw.decode_content = True # pragma: no cover
    def raise_for_status(self): # pragma: no cover
        pass # pragma: no cover
    def close(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
def mock_get(url, stream=False): # pragma: no cover
    content = ( # pragma: no cover
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\x06bKGD\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x00\tPHYS\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07tIME\x07\xe5\x04\x03\x14\n\x0c\x0ch\x93=\x00\x00\x00\x0eIDATx\xda\x636\x00\x00\x00\x02\x00\x01\xe2!\xbc\x33\x00\x00\x00\x00IEND\xaeB`\x82' # pragma: no cover
    ) # A simple 1x1 pixel PNG image # pragma: no cover
    return MockResponse(content) # pragma: no cover
 # pragma: no cover
requests.get = mock_get # pragma: no cover

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

