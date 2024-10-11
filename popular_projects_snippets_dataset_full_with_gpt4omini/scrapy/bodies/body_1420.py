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
