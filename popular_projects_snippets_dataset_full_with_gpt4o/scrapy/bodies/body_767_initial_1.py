from pprint import PrettyPrinter # pragma: no cover
from typing import Any, Dict, List # pragma: no cover
class ItemAdapter: # pragma: no cover
    def __init__(self, item: Any): # pragma: no cover
        self.item = item # pragma: no cover
    def asdict(self) -> Dict: # pragma: no cover
        return self.item # pragma: no cover
colour = False # pragma: no cover

lvl = 'example_lvl' # pragma: no cover
self = type('Mock', (object,), {'items': {'example_lvl': [{'name': 'item1'}, {'name': 'item2'}], 'another_lvl': [{'name': 'item3'}]}})() # pragma: no cover
display = type('Mock', (object,), {'pprint': PrettyPrinter().pprint})() # pragma: no cover
colour = False # pragma: no cover
ItemAdapter = ItemAdapter # pragma: no cover

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
