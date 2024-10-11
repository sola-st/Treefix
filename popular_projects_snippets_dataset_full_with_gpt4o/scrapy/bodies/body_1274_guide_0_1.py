from scrapy.exceptions import NotConfigured # pragma: no cover
class MockCrawlerSettings: # pragma: no cover
    def __init__(self, settings): # pragma: no cover
        self.settings = settings # pragma: no cover
    def getbool(self, name): # pragma: no cover
        return self.settings.get(name, False) # pragma: no cover
    def get(self, name, default=None): # pragma: no cover
        return self.settings.get(name, default) # pragma: no cover

settings = { # pragma: no cover
    'ROBOTSTXT_OBEY': False, # pragma: no cover
    'USER_AGENT': 'ScrapyTestAgent', # pragma: no cover
    'ROBOTSTXT_USER_AGENT': 'ScrapyRobot', # pragma: no cover
    'ROBOTSTXT_PARSER': 'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware' # pragma: no cover
} # pragma: no cover
crawler = MockCrawlerSettings(settings) # pragma: no cover
self = type('Mock', (object,), {'_default_useragent': None, '_robotstxt_useragent': None, 'crawler': None, '_parsers': None, '_parserimpl': None})() # pragma: no cover

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
