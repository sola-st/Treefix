from unittest.mock import Mock # pragma: no cover

crawler = Mock() # pragma: no cover
crawler.settings = Mock() # pragma: no cover
crawler.settings.getint = Mock(return_value=1) # pragma: no cover
# This will ensure the first uncovered path is executed # pragma: no cover
self = Mock() # pragma: no cover
self.__class__ = 'MockClass' # pragma: no cover
slot_startprios = ['incorrect_type'] # pragma: no cover
# This will ensure the second uncovered path is executed # pragma: no cover
DownloaderInterface = Mock() # pragma: no cover
downstream_queue_cls = Mock() # pragma: no cover
key = 'mock_key' # pragma: no cover
self.pqfactory = Mock(return_value=Mock()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
if crawler.settings.getint('CONCURRENT_REQUESTS_PER_IP') != 0:
    _l_(17412)

    raise ValueError(f'"{self.__class__}" does not support CONCURRENT_REQUESTS_PER_IP')
    _l_(17411)

if slot_startprios and not isinstance(slot_startprios, dict):
    _l_(17414)

    raise ValueError("DownloaderAwarePriorityQueue accepts "
                     "``slot_startprios`` as a dict; "
                     f"{slot_startprios.__class__!r} instance "
                     "is passed. Most likely, it means the state is"
                     "created by an incompatible priority queue. "
                     "Only a crawl started with the same priority "
                     "queue class can be resumed.")
    _l_(17413)

self._downloader_interface = DownloaderInterface(crawler)
_l_(17415)
self.downstream_queue_cls = downstream_queue_cls
_l_(17416)
self.key = key
_l_(17417)
self.crawler = crawler
_l_(17418)

self.pqueues = {}  # slot -> priority queue
_l_(17419)  # slot -> priority queue
for slot, startprios in (slot_startprios or {}).items():
    _l_(17421)

    self.pqueues[slot] = self.pqfactory(slot, startprios)
    _l_(17420)
