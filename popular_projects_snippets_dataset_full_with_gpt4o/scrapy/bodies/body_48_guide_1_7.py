from typing import Any # pragma: no cover

a: tuple = () # pragma: no cover
class MockBase:# pragma: no cover
  def __init__(self, *a, **kw):# pragma: no cover
    pass # pragma: no cover
class Mock(MockBase):# pragma: no cover
  pass # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exceptions.py
from l3.Runtime import _l_
self.print_help = kw.pop('print_help', True)
_l_(21639)
super().__init__(*a, **kw)
_l_(21640)
