from dataclasses import dataclass, field # pragma: no cover
from typing import Dict, List # pragma: no cover
class Display: # pragma: no cover
    def pprint(self, items, colorize: bool): # pragma: no cover
        for item in items: # pragma: no cover
            print(item) # pragma: no cover
class ItemAdapter: # pragma: no cover
    def __init__(self, item): # pragma: no cover
        self.item = item # pragma: no cover
    def asdict(self): # pragma: no cover
        return dict(self.item) # pragma: no cover

lvl = None # pragma: no cover
self = type('MockSelf', (object,), {'items': {'A': [{'name': 'item1'}, {'name': 'item2'}], 'B': [{'name': 'item3'}]}})() # pragma: no cover
display = type('MockDisplay', (Display,), {})() # pragma: no cover
colour = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
from l3.Runtime import _l_
if lvl is None:
    _l_(19990)

    items = [item for lst in self.items.values() for item in lst]
    _l_(19988)
else:
    items = self.items.get(lvl, [])
    _l_(19989)

print("# Scraped Items ", "-" * 60)
_l_(19991)
display.pprint([ItemAdapter(x).asdict() for x in items], colorize=colour)
_l_(19992)
