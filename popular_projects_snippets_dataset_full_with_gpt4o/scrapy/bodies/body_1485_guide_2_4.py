# This initialization ensures the uncovered path with NotImplementedError is handled. # pragma: no cover
try: # pragma: no cover
    raise NotImplementedError() # pragma: no cover
except NotImplementedError: # pragma: no cover
    pass  # This ensures the NotImplementedError is caught and handled. # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(16928)
