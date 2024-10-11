from scrapy.crawler import Crawler # pragma: no cover

self = type('MockSelf', (object,), {'__class__': type('MockClass', (object,), {}), 'pqfactory': lambda slot, startprios: 'priority_queue'})() # pragma: no cover
slot_startprios = {'slot1': 1, 'slot2': 2} # pragma: no cover
downstream_queue_cls = 'mock_downstream_queue_class' # pragma: no cover
key = 'my_unique_key' # pragma: no cover

class MockSettings:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = {'CONCURRENT_REQUESTS_PER_IP': 0}# pragma: no cover
    def getint(self, key):# pragma: no cover
        return self.settings.get(key, 0) # pragma: no cover
class MockCrawler:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = MockSettings() # pragma: no cover
class DownloaderInterface:# pragma: no cover
    def __init__(self, crawler):# pragma: no cover
        self.crawler = crawler # pragma: no cover

crawler = MockCrawler() # pragma: no cover
self = type('MockSelf', (object,), {'__class__': type('MockClass', (object,), {}), '_downloader_interface': None, 'downstream_queue_cls': None, 'key': None, 'pqueues': {}, 'pqfactory': lambda slot, startprios: f'PriorityQueueFor({slot}, {startprios})'})() # pragma: no cover
slot_startprios = {'slot1': 5, 'slot2': 3} # pragma: no cover
downstream_queue_cls = 'MockDownstreamQueue' # pragma: no cover
key = 'some_key' # pragma: no cover

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
