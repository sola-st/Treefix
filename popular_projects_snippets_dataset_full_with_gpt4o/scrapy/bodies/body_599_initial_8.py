import struct # pragma: no cover
from gzip import GzipFile # pragma: no cover
from io import BytesIO # pragma: no cover

data = b'This is some gzipped data' # pragma: no cover
class MockStructError(Exception): pass # pragma: no cover
struct.error = MockStructError # pragma: no cover

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
