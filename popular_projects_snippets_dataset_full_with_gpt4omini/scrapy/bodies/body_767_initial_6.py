from typing import List, Any # pragma: no cover
from unittest.mock import Mock # pragma: no cover

lvl = None # pragma: no cover
self = Mock(spec=object, items={'level1': ['item1', 'item2'], 'level2': ['item3']}) # pragma: no cover
display = Mock() # pragma: no cover
colour = 'green' # pragma: no cover
class ItemAdapter:# pragma: no cover
    def __init__(self, item: Any):# pragma: no cover
        self.item = item# pragma: no cover
    def asdict(self):# pragma: no cover
        return {'item': self.item} # pragma: no cover

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
