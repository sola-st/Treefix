# Ensuring NotImplementedError is executed as intended # pragma: no cover
try: # pragma: no cover
    raise NotImplementedError() # pragma: no cover
except NotImplementedError: # pragma: no cover
    print('NotImplementedError was raised and handled.') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(16928)
