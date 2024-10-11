from typing import List, Optional # pragma: no cover
from pprint import PrettyPrinter # pragma: no cover

lvl: Optional[int] = None # pragma: no cover
self = type('Mock', (object,), {'items': {1: ['item1', 'item2'], 2: ['item3']}})() # pragma: no cover
display = PrettyPrinter() # pragma: no cover
colour = 'green' # pragma: no cover
ItemAdapter = type('ItemAdapter', (object,), {'__init__': lambda self, x: None, 'asdict': lambda self: {'item': x}}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
from l3.Runtime import _l_
if lvl is None:
    _l_(8897)

    items = [item for lst in self.items.values() for item in lst]
    _l_(8895)
else:
    items = self.items.get(lvl, [])
    _l_(8896)

print("# Scraped Items ", "-" * 60)
_l_(8898)
display.pprint([ItemAdapter(x).asdict() for x in items], colorize=colour)
_l_(8899)
