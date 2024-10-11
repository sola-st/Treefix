import sys # pragma: no cover

text = 123 # pragma: no cover
encoding = None # pragma: no cover
errors = 'strict' # pragma: no cover
exit = sys.exit # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
from l3.Runtime import _l_
"""Return the unicode representation of a bytes object ``text``. If
    ``text`` is already an unicode object, return it as-is."""
if isinstance(text, str):
    _l_(18782)

    aux = text
    _l_(18781)
    exit(aux)
if not isinstance(text, (bytes, str)):
    _l_(18784)

    raise TypeError('to_unicode must receive a bytes or str '
                    f'object, got {type(text).__name__}')
    _l_(18783)
if encoding is None:
    _l_(18786)

    encoding = 'utf-8'
    _l_(18785)
aux = text.decode(encoding, errors)
_l_(18787)
exit(aux)
