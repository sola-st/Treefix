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
