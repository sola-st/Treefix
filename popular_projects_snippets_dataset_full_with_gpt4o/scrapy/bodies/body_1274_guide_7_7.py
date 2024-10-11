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
    def __init__(self, settings_dict): # pragma: no cover
        self.settings = MockSettings(settings_dict) # pragma: no cover
 # pragma: no cover
class MockParserImpl: # pragma: no cover
    @staticmethod # pragma: no cover
    def from_crawler(crawler, data): # pragma: no cover
        if isinstance(data, bytes) and data: # pragma: no cover
            return MockParserImpl() # pragma: no cover
        raise ValueError('Invalid data') # pragma: no cover
 # pragma: no cover
def load_object(path): # pragma: no cover
    if path == 'MockParserImpl': # pragma: no cover
        return MockParserImpl # pragma: no cover
    raise ImportError(f'Cannot load object {path}') # pragma: no cover
 # pragma: no cover
settings_dict = { # pragma: no cover
    'ROBOTSTXT_OBEY': False, # pragma: no cover
    'USER_AGENT': 'ScrapyTestAgent', # pragma: no cover
    'ROBOTSTXT_USER_AGENT': 'ScrapyRobot', # pragma: no cover
    'ROBOTSTXT_PARSER': 'MockParserImpl' # pragma: no cover
} # pragma: no cover
crawler = MockCrawler(settings_dict) # pragma: no cover
self = type('Mock', (object,), {'_default_useragent': 'ScrapyTestAgent', '_robotstxt_useragent': 'ScrapyRobot', 'crawler': crawler, '_parsers': {}, '_parserimpl': MockParserImpl})() # pragma: no cover

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
