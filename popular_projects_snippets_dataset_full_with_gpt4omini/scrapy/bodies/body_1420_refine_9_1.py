from typing import List, Dict # pragma: no cover

class MockDownloaderInterface:# pragma: no cover
    def stats(self, pqueues):# pragma: no cover
        return [(len(queue), index) for index, queue in enumerate(pqueues)]# pragma: no cover
# pragma: no cover
class MockQueue:# pragma: no cover
    def __init__(self, items):# pragma: no cover
        self.items = items# pragma: no cover
    def peek(self):# pragma: no cover
        return self.items[0] if self.items else None# pragma: no cover

from typing import List, Dict # pragma: no cover

class MockDownloaderInterface:# pragma: no cover
    def stats(self, pqueues):# pragma: no cover
        return [(len(queue.items), index) for index, queue in enumerate(pqueues)] # pragma: no cover
class MockQueue:# pragma: no cover
    def __init__(self, items):# pragma: no cover
        self.items = items# pragma: no cover
    def peek(self):# pragma: no cover
        return self.items[0] if self.items else None # pragma: no cover
mock_downloader_interface = MockDownloaderInterface() # pragma: no cover
mock_queues = [MockQueue([1, 2, 3]), MockQueue([]), MockQueue([4, 5])] # pragma: no cover
self = type('Mock', (), {'_downloader_interface': mock_downloader_interface, 'pqueues': mock_queues})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
"""Returns the next object to be returned by :meth:`pop`,
        but without removing it from the queue.

        Raises :exc:`NotImplementedError` if the underlying queue class does
        not implement a ``peek`` method, which is optional for queues.
        """
stats = self._downloader_interface.stats(self.pqueues)
_l_(8202)
if not stats:
    _l_(8204)

    aux = None
    _l_(8203)
    exit(aux)
slot = min(stats)[1]
_l_(8205)
queue = self.pqueues[slot]
_l_(8206)
aux = queue.peek()
_l_(8207)
exit(aux)
