from typing import List # pragma: no cover

row_ = ['example1', 'example2', 'example3'] # pragma: no cover
def to_unicode(value, encoding): return str(value).encode(encoding).decode(encoding) # pragma: no cover
encoding = 'utf-8' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from l3.Runtime import _l_
aux = [to_unicode(field, encoding) for field in row_]
_l_(8834)
exit(aux)
