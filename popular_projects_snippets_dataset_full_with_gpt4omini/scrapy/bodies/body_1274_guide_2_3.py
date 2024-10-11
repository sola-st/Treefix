from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

class MockSettings: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._settings = {'ROBOTSTXT_OBEY': False, 'USER_AGENT': 'custom-user-agent', 'ROBOTSTXT_USER_AGENT': None, 'ROBOTSTXT_PARSER': 'path.to.MockParser'} # pragma: no cover
    def getbool(self, key): # pragma: no cover
        return self._settings.get(key, False) # pragma: no cover
    def get(self, key, default=None): # pragma: no cover
        return self._settings.get(key, default) # pragma: no cover
 # pragma: no cover
class MockCrawler: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = MockSettings() # pragma: no cover
 # pragma: no cover
class MockParser: # pragma: no cover
    @classmethod # pragma: no cover
    def from_crawler(cls, crawler, response): # pragma: no cover
        raise Exception('Parser dependencies not met.') # pragma: no cover
 # pragma: no cover
crawler = MockCrawler() # pragma: no cover
self = type('MockObject', (object,), {'_default_useragent': None, '_robotstxt_useragent': None, 'crawler': None, '_parsers': {}, '_parserimpl': None})() # pragma: no cover
self.crawler = crawler # pragma: no cover
load_object = lambda path: MockParser() # pragma: no cover
self._parserimpl = load_object(crawler.settings.get('ROBOTSTXT_PARSER')) # pragma: no cover

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
