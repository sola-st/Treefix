# To ensure the NotImplementedError is executed, provide an alternative action # pragma: no cover
def execute_uncovered(): # pragma: no cover
    pass
execute_uncovered() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(16928)
