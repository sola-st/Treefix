from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.project import get_project_settings # pragma: no cover

crawler = type('MockCrawler', (object,), {'settings': get_project_settings()})() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
load_object = lambda path: type('MockParser', (object,), {'from_crawler': lambda self, x, y: None}) # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover

class MockSettings:# pragma: no cover
    def getbool(self, key):# pragma: no cover
        if key == 'ROBOTSTXT_OBEY':# pragma: no cover
            return False# pragma: no cover
        return None# pragma: no cover
    def get(self, key, default=None):# pragma: no cover
        settings = {'USER_AGENT': 'Scrapy', 'ROBOTSTXT_USER_AGENT': None, 'ROBOTSTXT_PARSER': 'my_parser'}# pragma: no cover
        return settings.get(key, default)# pragma: no cover
# pragma: no cover
crawler = type('MockCrawler', (object,), {'settings': MockSettings()})() # pragma: no cover
NotConfigured = NotConfigured() # pragma: no cover
self = type('MockSelf', (object,), {'_default_useragent': None, '_robotstxt_useragent': None, 'crawler': crawler, '_parsers': {}, '_parserimpl': None})() # pragma: no cover
def load_object(name):# pragma: no cover
    class MockParser:# pragma: no cover
        @classmethod# pragma: no cover
        def from_crawler(cls, crawler, response):# pragma: no cover
            pass# pragma: no cover
    return MockParser# pragma: no cover
self._parserimpl = load_object('my_parser') # pragma: no cover

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
