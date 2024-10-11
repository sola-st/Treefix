row_ = ['field_1', 'field_2', 'field_3'] # pragma: no cover
def to_unicode(field, encoding): return str(field).encode(encoding).decode(encoding) # pragma: no cover
encoding = 'utf-8' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from l3.Runtime import _l_
aux = [to_unicode(field, encoding) for field in row_]
_l_(19818)
exit(aux)
