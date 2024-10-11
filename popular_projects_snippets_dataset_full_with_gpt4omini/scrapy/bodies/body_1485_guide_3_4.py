import unittest # pragma: no cover

class MockedException(Exception): pass # pragma: no cover
def trigger_exception(): # pragma: no cover
    pass
trigger_exception() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
