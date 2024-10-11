# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/gz.py
from l3.Runtime import _l_
"""Gunzip the given data and return as much data as possible.

    This is resilient to CRC checksum errors.
    """
f = GzipFile(fileobj=BytesIO(data))
_l_(7656)
output_list = []
_l_(7657)
chunk = b'.'
_l_(7658)
while chunk:
    _l_(7669)

    try:
        _l_(7668)

        chunk = f.read1(8196)
        _l_(7659)
        output_list.append(chunk)
        _l_(7660)
    except (IOError, EOFError, struct.error):
        _l_(7667)

        # complete only if there is some data, otherwise re-raise
        # see issue 87 about catching struct.error
        # some pages are quite small so output_list is empty and f.extrabuf
        # contains the whole page content
        if output_list or getattr(f, 'extrabuf', None):
            _l_(7666)

            try:
                _l_(7664)

                output_list.append(f.extrabuf[-f.extrasize:])
                _l_(7661)
            finally:
                _l_(7663)

                break
                _l_(7662)
        else:
            raise
            _l_(7665)
aux = b''.join(output_list)
_l_(7670)
exit(aux)
