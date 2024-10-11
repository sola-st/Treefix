from scrapy.exceptions import NotConfigured # pragma: no cover

crawler = type('MockCrawler', (object,), {'settings': {'ROBOTSTXT_OBEY': False, 'USER_AGENT': 'ScrapyBot', 'ROBOTSTXT_USER_AGENT': None, 'ROBOTSTXT_PARSER': 'some.parser.Module'}})() # pragma: no cover
NotConfigured = NotConfigured # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
load_object = lambda x: type('MockParser', (object,), {'from_crawler': lambda self, crawler, data: None})() # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.settings import Settings # pragma: no cover

settings = Settings() # pragma: no cover
settings.set('ROBOTSTXT_OBEY', False) # pragma: no cover
settings.set('USER_AGENT', 'ScrapyBot') # pragma: no cover
settings.set('ROBOTSTXT_USER_AGENT', None) # pragma: no cover
settings.set('ROBOTSTXT_PARSER', 'someparser') # pragma: no cover
crawler = type('MockCrawler', (object,), {'settings': settings})() # pragma: no cover
NotConfigured = NotConfigured() # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self._default_useragent = settings.get('USER_AGENT') # pragma: no cover
self._robotstxt_useragent = settings.get('ROBOTSTXT_USER_AGENT') # pragma: no cover
self.crawler = crawler # pragma: no cover
self._parsers = {} # pragma: no cover

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
