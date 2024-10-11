from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover
from scrapy.settings import Settings # pragma: no cover

class MockSettings: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._settings = { # pragma: no cover
            'ROBOTSTXT_OBEY': False, # pragma: no cover
            'USER_AGENT': 'my-user-agent', # pragma: no cover
            'ROBOTSTXT_USER_AGENT': None, # pragma: no cover
            'ROBOTSTXT_PARSER': 'path.to.MockParser' # pragma: no cover
        } # pragma: no cover
    def getbool(self, key): # pragma: no cover
        return self._settings.get(key, False) # pragma: no cover
    def get(self, key, default=None): # pragma: no cover
        return self._settings.get(key, default) # pragma: no cover
class MockParser: # pragma: no cover
    @classmethod # pragma: no cover
    def from_crawler(cls, crawler, response): # pragma: no cover
        pass # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._default_useragent = None # pragma: no cover
self._robotstxt_useragent = None # pragma: no cover
self.crawler = type('MockCrawler', (object,), {'settings': MockSettings()})() # pragma: no cover
self._parsers = {} # pragma: no cover
load_object = lambda path: MockParser() # pragma: no cover
self._parserimpl = load_object(self.crawler.settings.get('ROBOTSTXT_PARSER')) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/robotstxt.py
from l3.Runtime import _l_
if not crawler.settings.getbool('ROBOTSTXT_OBEY'):
    _l_(9808)

    raise NotConfigured
    _l_(9807)
self._default_useragent = crawler.settings.get('USER_AGENT', 'Scrapy')
_l_(9809)
self._robotstxt_useragent = crawler.settings.get('ROBOTSTXT_USER_AGENT', None)
_l_(9810)
self.crawler = crawler
_l_(9811)
self._parsers = {}
_l_(9812)
self._parserimpl = load_object(crawler.settings.get('ROBOTSTXT_PARSER'))
_l_(9813)

# check if parser dependencies are met, this should throw an error otherwise.
self._parserimpl.from_crawler(self.crawler, b'')
_l_(9814)
