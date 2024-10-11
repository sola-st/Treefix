import struct # pragma: no cover
from gzip import GzipFile # pragma: no cover
from io import BytesIO # pragma: no cover

data = b"\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03\xf3H\xcd\xc9\xc9\x57(\xcf/\xcaI\x01\x00\x85\x11\x4a\xd8\x0b\x00\x00\x00" # pragma: no cover
struct.error = type("Mock", (Exception,), {}) # pragma: no cover

from gzip import GzipFile # pragma: no cover
from io import BytesIO # pragma: no cover
import struct # pragma: no cover

data = b"\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03\x0b\xc9\xc8\x2c\x56\x00\xa2\xe2\xcc\x92\xdc\xc4\x92\x54\x85\x92\xd4\xe2\x12\x85\xb4\xcc\xfc\x3c\x85\x92\x9c\x4a\x85\x92\xc4\x92\xd2\x62\x01\x00\x2f\xd5\xff\x9e\x1e\x00\x00\x00" # pragma: no cover
struct.error = type('Mock', (Exception,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/gz.py
from l3.Runtime import _l_
"""Gunzip the given data and return as much data as possible.

    This is resilient to CRC checksum errors.
    """
f = GzipFile(fileobj=BytesIO(data))
_l_(18494)
output_list = []
_l_(18495)
chunk = b'.'
_l_(18496)
while chunk:
    _l_(18507)

    try:
        _l_(18506)

        chunk = f.read1(8196)
        _l_(18497)
        output_list.append(chunk)
        _l_(18498)
    except (IOError, EOFError, struct.error):
        _l_(18505)

        # complete only if there is some data, otherwise re-raise
        # see issue 87 about catching struct.error
        # some pages are quite small so output_list is empty and f.extrabuf
        # contains the whole page content
        if output_list or getattr(f, 'extrabuf', None):
            _l_(18504)

            try:
                _l_(18502)

                output_list.append(f.extrabuf[-f.extrasize:])
                _l_(18499)
            finally:
                _l_(18501)

                break
                _l_(18500)
        else:
            raise
            _l_(18503)
aux = b''.join(output_list)
_l_(18508)
exit(aux)
