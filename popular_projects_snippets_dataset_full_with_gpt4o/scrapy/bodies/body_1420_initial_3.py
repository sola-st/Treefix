from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
self._downloader_interface = Mock() # pragma: no cover
self.pqueues = [Mock(peek=Mock(return_value='example_peek_value'))] # pragma: no cover
self._downloader_interface.stats = Mock(return_value=[('mock_key', 0)]) # pragma: no cover

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
