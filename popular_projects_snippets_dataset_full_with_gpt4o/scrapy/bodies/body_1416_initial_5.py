from collections import defaultdict # pragma: no cover

crawler = type('Mock', (object,), {'settings': type('Mock', (object,), {'getint': lambda self, key: 0})()})() # pragma: no cover
self = type('Mock', (object,), {'__class__': 'MockClass', '_downloader_interface': None, 'downstream_queue_cls': None, 'key': None, 'crawler': None, 'pqueues': {}, 'pqfactory': lambda self, slot, startprios: f'PriorityQueue for {slot}'})() # pragma: no cover
slot_startprios = {'slot1': 10, 'slot2': 20} # pragma: no cover
DownloaderInterface = lambda crawler: f'Downloader interface for {crawler}' # pragma: no cover
downstream_queue_cls = 'MockQueueClass' # pragma: no cover
key = 'mock_key' # pragma: no cover

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
