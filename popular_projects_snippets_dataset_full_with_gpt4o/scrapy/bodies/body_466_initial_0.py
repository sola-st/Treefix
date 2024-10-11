import sys # pragma: no cover
import codecs # pragma: no cover

row_ = ['name', 'age', 'city'] # pragma: no cover
to_unicode = codecs.decode # pragma: no cover
encoding = 'utf-8' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/iterators.py
from l3.Runtime import _l_
aux = [to_unicode(field, encoding) for field in row_]
_l_(19818)
exit(aux)
