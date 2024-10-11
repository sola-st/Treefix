import asyncio # pragma: no cover

def set_asyncio_event_loop(loop): # pragma: no cover
    asyncio.set_event_loop(loop) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
from l3.Runtime import _l_
aux = set_asyncio_event_loop(None)
_l_(18417)
exit(aux)
