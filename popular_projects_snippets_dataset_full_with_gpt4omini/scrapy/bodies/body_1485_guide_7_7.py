import sys # pragma: no cover

class CustomNotImplementedError(NotImplementedError): pass # pragma: no cover
def invoke_error(): # pragma: no cover
    pass
invoke_error() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
