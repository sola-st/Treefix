from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

class MockSettings:# pragma: no cover
    def getbool(self, key): return False# pragma: no cover
    def get(self, key, default=None):# pragma: no cover
        settings = {'USER_AGENT': 'Scrapy', 'ROBOTSTXT_USER_AGENT': None, 'ROBOTSTXT_PARSER': 'module.ClassName'}# pragma: no cover
        return settings.get(key, default)# pragma: no cover
# pragma: no cover
class MockCrawler:# pragma: no cover
    settings = MockSettings()# pragma: no cover
# pragma: no cover
crawler = MockCrawler() # pragma: no cover
NotConfigured = Exception('Configuration not set') # pragma: no cover
self = type('Mock', (object,), { '_default_useragent': None, '_robotstxt_useragent': None, 'crawler': None, '_parsers': {}, '_parserimpl': None })() # pragma: no cover
def mock_load_object(path):# pragma: no cover
    class DummyParser:# pragma: no cover
        @classmethod# pragma: no cover
        def from_crawler(cls, crawler, response):# pragma: no cover
            pass# pragma: no cover
    return DummyParser# pragma: no cover
load_object = mock_load_object # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

class MockSettings:# pragma: no cover
    def getbool(self, key): return False# pragma: no cover
    def get(self, key, default=None):# pragma: no cover
        if key == 'ROBOTSTXT_OBEY':# pragma: no cover
            return False# pragma: no cover
        if key == 'USER_AGENT':# pragma: no cover
            return 'Scrapy'# pragma: no cover
        if key == 'ROBOTSTXT_USER_AGENT':# pragma: no cover
            return None# pragma: no cover
        if key == 'ROBOTSTXT_PARSER':# pragma: no cover
            return 'mock_parser'# pragma: no cover
        return default# pragma: no cover
# pragma: no cover
class MockCrawler:# pragma: no cover
    settings = MockSettings()# pragma: no cover
# pragma: no cover
crawler = MockCrawler() # pragma: no cover
class NotConfigured(Exception):# pragma: no cover
    pass # pragma: no cover
self = type('MockSelf', (object,), {'_default_useragent': 'Scrapy', '_robotstxt_useragent': None, 'crawler': None, '_parsers': {}, '_parserimpl': None})() # pragma: no cover
def mock_load_object(path):# pragma: no cover
    class DummyParser:# pragma: no cover
        @classmethod# pragma: no cover
        def from_crawler(cls, crawler, response): pass# pragma: no cover
    return DummyParser# pragma: no cover
load_object = mock_load_object # pragma: no cover
self.crawler = crawler # pragma: no cover
self._parserimpl = load_object('mock_parser') # pragma: no cover

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
