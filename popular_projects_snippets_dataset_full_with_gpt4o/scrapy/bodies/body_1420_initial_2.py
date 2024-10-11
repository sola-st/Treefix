import random # pragma: no cover

class MockDownloaderInterface: # pragma: no cover
    def stats(self, pqueues): # pragma: no cover
        return {i: (random.randint(0, 100), i) for i in range(len(pqueues))} # pragma: no cover
 # pragma: no cover
class MockQueue: # pragma: no cover
    def peek(self): # pragma: no cover
        return 'peek_output' # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_downloader_interface': MockDownloaderInterface(), # pragma: no cover
    'pqueues': [MockQueue() for _ in range(5)] # pragma: no cover
}) # pragma: no cover

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
