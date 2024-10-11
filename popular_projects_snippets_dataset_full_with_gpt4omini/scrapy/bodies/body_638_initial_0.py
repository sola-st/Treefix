import asyncio # pragma: no cover

def set_asyncio_event_loop(loop): asyncio.set_event_loop(loop) # pragma: no cover
set_asyncio_event_loop(asyncio.new_event_loop()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
from l3.Runtime import _l_
aux = set_asyncio_event_loop(None)
_l_(7514)
exit(aux)
