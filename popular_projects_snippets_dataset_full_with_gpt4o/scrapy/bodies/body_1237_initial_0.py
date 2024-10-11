from typing import Optional, Any # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self, indent: Optional[int], new_item: bool): # pragma: no cover
        self.indent = indent # pragma: no cover
        self.xg = type('XG', (object,), {'characters': lambda self, text: print(f'characters called with: {text}')})() # pragma: no cover
new_item: bool = True # pragma: no cover
self = Mock(indent=2, new_item=new_item) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exporters.py
from l3.Runtime import _l_
if self.indent is not None and (self.indent > 0 or new_item):
    _l_(21106)

    self.xg.characters('\n')
    _l_(21105)
