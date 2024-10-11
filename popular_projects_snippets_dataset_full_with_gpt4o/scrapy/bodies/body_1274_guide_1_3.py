from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

class MockSettings: # pragma: no cover
    def __init__(self, settings_dict): # pragma: no cover
        self.settings_dict = settings_dict # pragma: no cover
    def getbool(self, key): # pragma: no cover
        return self.settings_dict.get(key, False) # pragma: no cover
    def get(self, key, default=None): # pragma: no cover
        return self.settings_dict.get(key, default) # pragma: no cover
 # pragma: no cover
class MockCrawler: # pragma: no cover
    def __init__(self, settings): # pragma: no cover
        self.settings = settings # pragma: no cover
 # pragma: no cover
class MockParserImpl: # pragma: no cover
    @classmethod # pragma: no cover
    def from_crawler(cls, crawler, data): # pragma: no cover
        return cls() # pragma: no cover
 # pragma: no cover
settings_dict = { # pragma: no cover
    'ROBOTSTXT_OBEY': False, # pragma: no cover
    'USER_AGENT': 'Scrapy', # pragma: no cover
    'ROBOTSTXT_USER_AGENT': None, # pragma: no cover
    'ROBOTSTXT_PARSER': 'MockParserImpl' # pragma: no cover
} # pragma: no cover
 # pragma: no cover
crawler = MockCrawler(MockSettings(settings_dict)) # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self._default_useragent = None # pragma: no cover
self._robotstxt_useragent = None # pragma: no cover
self.crawler = None # pragma: no cover
self._parsers = None # pragma: no cover
self._parserimpl = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/robotstxt.py
from l3.Runtime import _l_
if not crawler.settings.getbool('ROBOTSTXT_OBEY'):
    _l_(21282)

    raise NotConfigured
    _l_(21281)
self._default_useragent = crawler.settings.get('USER_AGENT', 'Scrapy')
_l_(21283)
self._robotstxt_useragent = crawler.settings.get('ROBOTSTXT_USER_AGENT', None)
_l_(21284)
self.crawler = crawler
_l_(21285)
self._parsers = {}
_l_(21286)
self._parserimpl = load_object(crawler.settings.get('ROBOTSTXT_PARSER'))
_l_(21287)

# check if parser dependencies are met, this should throw an error otherwise.
self._parserimpl.from_crawler(self.crawler, b'')
_l_(21288)
