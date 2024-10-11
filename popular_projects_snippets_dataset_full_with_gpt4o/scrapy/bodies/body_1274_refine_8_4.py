from scrapy.exceptions import NotConfigured # pragma: no cover

crawler = type('MockCrawler', (object,), {'settings': type('MockSettings', (object,), {'getbool': lambda self, key: True, 'get': lambda self, key, default=None: 'test_parser' if key == 'ROBOTSTXT_PARSER' else default})()})() # pragma: no cover
self = type('MockSelf', (object,), {'_default_useragent': None, '_robotstxt_useragent': None, 'crawler': None, '_parsers': None, '_parserimpl': None})() # pragma: no cover
load_object = lambda path: type('MockParser', (object,), {'from_crawler': lambda cls, crawler, b: None}) # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

crawler = type('MockCrawler', (object,), {'settings': type('MockSettings', (object,), {'getbool': lambda self, key: True, 'get': lambda self, key, default=None: 'Scrapy'})()})() # pragma: no cover
self = type('MockSelf', (object,), {'_default_useragent': None, '_robotstxt_useragent': None, 'crawler': None, '_parsers': None, '_parserimpl': None})() # pragma: no cover
self._default_useragent = '' # pragma: no cover
self._robotstxt_useragent = None # pragma: no cover
self.crawler = crawler # pragma: no cover
self._parsers = {} # pragma: no cover
self._parserimpl = type('MockParserImpl', (object,), {'from_crawler': lambda crawler, b: None})() # pragma: no cover

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
