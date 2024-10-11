from typing import List, Dict, Any # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
self._downloader_interface = type('MockDownloaderInterface', (object,), {'stats': lambda self, pqueues: {0: (5, 0), 1: (3, 1)} if pqueues else None})() # pragma: no cover
self.pqueues = type('MockPQueues', (dict,), {0: type('MockQueue', (object,), {'peek': lambda self: 'next_item'})(), 1: type('MockQueue', (object,), {'peek': lambda self: 'another_item'})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
"""Returns the next object to be returned by :meth:`pop`,
        but without removing it from the queue.

        Raises :exc:`NotImplementedError` if the underlying queue class does
        not implement a ``peek`` method, which is optional for queues.
        """
stats = self._downloader_interface.stats(self.pqueues)
_l_(19414)
if not stats:
    _l_(19416)

    aux = None
    _l_(19415)
    exit(aux)
slot = min(stats)[1]
_l_(19417)
queue = self.pqueues[slot]
_l_(19418)
aux = queue.peek()
_l_(19419)
exit(aux)
