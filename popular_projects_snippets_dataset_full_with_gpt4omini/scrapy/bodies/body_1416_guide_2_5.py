class MockCrawler: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = {'CONCURRENT_REQUESTS_PER_IP': 0} # pragma: no cover
class DownloaderInterface: # pragma: no cover
    def __init__(self, crawler): # pragma: no cover
        self.crawler = crawler # pragma: no cover

crawler = MockCrawler() # pragma: no cover
slot_startprios = None # pragma: no cover
downstream_queue_cls = None # pragma: no cover
key = 'mock_key' # pragma: no cover
self = type('MockClass', (object,), {})() # pragma: no cover
self._downloader_interface = DownloaderInterface(crawler) # pragma: no cover
self.pqfactory = lambda slot, startprios: 'mock_priority_queue' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
from l3.Runtime import _l_
if crawler.settings.getint('CONCURRENT_REQUESTS_PER_IP') != 0:
    _l_(6618)

    raise ValueError(f'"{self.__class__}" does not support CONCURRENT_REQUESTS_PER_IP')
    _l_(6617)

if slot_startprios and not isinstance(slot_startprios, dict):
    _l_(6620)

    raise ValueError("DownloaderAwarePriorityQueue accepts "
                     "``slot_startprios`` as a dict; "
                     f"{slot_startprios.__class__!r} instance "
                     "is passed. Most likely, it means the state is"
                     "created by an incompatible priority queue. "
                     "Only a crawl started with the same priority "
                     "queue class can be resumed.")
    _l_(6619)

self._downloader_interface = DownloaderInterface(crawler)
_l_(6621)
self.downstream_queue_cls = downstream_queue_cls
_l_(6622)
self.key = key
_l_(6623)
self.crawler = crawler
_l_(6624)

self.pqueues = {}  # slot -> priority queue
_l_(6625)  # slot -> priority queue
for slot, startprios in (slot_startprios or {}).items():
    _l_(6627)

    self.pqueues[slot] = self.pqfactory(slot, startprios)
    _l_(6626)
