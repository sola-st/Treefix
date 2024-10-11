from PIL import Image # pragma: no cover

PIL = type('Mock', (object,), {'Image': Image}) # pragma: no cover

from PIL import Image # pragma: no cover
import requests # pragma: no cover

PIL = type('Mock', (object,), {'Image': Image})() # pragma: no cover
r = type('ResponseMock', (object,), {'content': b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x90\x00\x00\x00\xc8\x08\x06\x00\x00\x00\xea\x97\xdf\x10\x00\x00\x02\x1dIDATx\xda\xec\xbd\x7f\x98\x15\x0c\x04\xc0\xff\xf3\xa0\x8f{\x8c\xe3\x10\xc6\x9e\xff\x07\x93\xb0\x16\x24\x83\x17\xf8\x02\xa7V\x01\x78\x2b\x15\xd1\xd0\xc2\xdc\x10s\xd4\x96\xc2n\x04\x83\x8b\xe8w\xd7\x9a\x1d\xb8}\x1c\x7f\xafx-\x15\xab}\r5\x13\x97\x99\xb3\xa3\x86\xa6\x8b\x91\xa8N\x19\x80\x1d\x1f\x07\xb0\x00\x00\xe0\x1c\x0e!?\x10\x07&\x1d\x03s\r1\x8f\x11\x99\x05\x979Y\x90R\x1aS\xa8\x05\xd9\xfaZB\xc5\xcf\x054\xaa\xf0\x16\n\x05\x04\x00\x00\x00\x00IEND\xaeB`\x82'}), # pragma: no cover

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

