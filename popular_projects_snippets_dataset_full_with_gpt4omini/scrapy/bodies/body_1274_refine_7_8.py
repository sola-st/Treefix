from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.project import get_project_settings # pragma: no cover

crawler = type('MockCrawler', (object,), {'settings': get_project_settings()})() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
self = type('MockSelf', (object,), {'_default_useragent': '', '_robotstxt_useragent': '', 'crawler': None, '_parsers': {}, '_parserimpl': None})() # pragma: no cover
load_object = lambda x: type('MockParserImpl', (object,), {'from_crawler': lambda self, crawler, data: None})() # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover

class MockSettings:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.settings = { # pragma: no cover
            'ROBOTSTXT_OBEY': True, # pragma: no cover
            'USER_AGENT': 'Scrapy', # pragma: no cover
            'ROBOTSTXT_USER_AGENT': None, # pragma: no cover
            'ROBOTSTXT_PARSER': 'some.parser.Module', # pragma: no cover
        } # pragma: no cover
    def getbool(self, key): # pragma: no cover
        return self.settings.get(key, False) # pragma: no cover
    def get(self, key, default): # pragma: no cover
        return self.settings.get(key, default) # pragma: no cover
crawler = type('MockCrawler', (object,), {'settings': MockSettings()})() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
self = type('MockSelf', (object,), {'_default_useragent': 'Scrapy', '_robotstxt_useragent': None, 'crawler': None, '_parsers': {}, '_parserimpl': None})() # pragma: no cover
self.crawler = crawler # pragma: no cover
class SomeParser:  # pragma: no cover
    @staticmethod # pragma: no cover
    def from_crawler(crawler, data): # pragma: no cover
        pass # pragma: no cover
load_object = lambda name: SomeParser # pragma: no cover

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
