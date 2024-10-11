from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

class MockSettings: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = { # pragma: no cover
            'ROBOTSTXT_OBEY': False,  # This will trigger the NotConfigured exception # pragma: no cover
            'USER_AGENT': 'my-custom-user-agent', # pragma: no cover
            'ROBOTSTXT_USER_AGENT': None, # pragma: no cover
            'ROBOTSTXT_PARSER': 'mock_parser.MockParser' # pragma: no cover
        } # pragma: no cover
    def get(self, key, default=None): # pragma: no cover
        return self.settings.get(key, default) # pragma: no cover
    def getbool(self, key): # pragma: no cover
        return self.settings.get(key, False) # pragma: no cover
 # pragma: no cover
class MockParser: # pragma: no cover
    @classmethod # pragma: no cover
    def from_crawler(cls, crawler, response): # pragma: no cover
        raise Exception('Parser dependencies are not satisfied.') # pragma: no cover
# Simulate parser dependency issue # pragma: no cover
 # pragma: no cover
class MockCrawler: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = MockSettings() # pragma: no cover
 # pragma: no cover
crawler = MockCrawler() # pragma: no cover
self = type('Mock', (object,), {'_default_useragent': None, '_robotstxt_useragent': None, 'crawler': None, '_parsers': {}, '_parserimpl': None})() # pragma: no cover
self.crawler = crawler # pragma: no cover

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
