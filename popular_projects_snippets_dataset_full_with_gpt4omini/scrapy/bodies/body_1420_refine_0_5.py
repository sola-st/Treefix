from collections import deque # pragma: no cover

class MockDownloaderInterface:# pragma: no cover
    def stats(self, pqueues):# pragma: no cover
        return [(len(queue), idx) for idx, queue in enumerate(pqueues) if queue] # pragma: no cover
class MockQueue:# pragma: no cover
    def __init__(self, elements):# pragma: no cover
        self.elements = elements# pragma: no cover
    def peek(self):# pragma: no cover
        return self.elements[0] if self.elements else None # pragma: no cover

from collections import deque # pragma: no cover

class MockDownloaderInterface:# pragma: no cover
    def stats(self, pqueues):# pragma: no cover
        return [(len(queue.elements), idx) for idx, queue in enumerate(pqueues) if queue.elements] # pragma: no cover
class MockQueue:# pragma: no cover
    def __init__(self, elements):# pragma: no cover
        self.elements = elements# pragma: no cover
    def peek(self):# pragma: no cover
        return self.elements[0] if self.elements else None # pragma: no cover
self = type('MockObject', (), {})() # pragma: no cover
self._downloader_interface = MockDownloaderInterface() # pragma: no cover
self.pqueues = [MockQueue([1, 2, 3]), MockQueue([]), MockQueue([4, 5, 6])] # pragma: no cover

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
