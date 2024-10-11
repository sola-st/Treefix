from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover
from types import SimpleNamespace # pragma: no cover

crawler = SimpleNamespace(settings={'ROBOTSTXT_OBEY': False, 'USER_AGENT': 'MockUserAgent', 'ROBOTSTXT_USER_AGENT': 'MockRobotUserAgent', 'ROBOTSTXT_PARSER': 'mock_parser'}) # pragma: no cover
class MockCrawler:# pragma: no cover
    def __init__(self, settings):# pragma: no cover
        self.settings = settings# pragma: no cover
crawler = MockCrawler(settings={'ROBOTSTXT_OBEY': False, 'USER_AGENT': 'MockUserAgent', 'ROBOTSTXT_USER_AGENT': 'MockRobotUserAgent', 'ROBOTSTXT_PARSER': 'mock_parser'}) # pragma: no cover
self = type('Mock', (object,), {'_default_useragent': None, '_robotstxt_useragent': None, 'crawler': None, '_parsers': None, '_parserimpl': None})() # pragma: no cover
def mock_parser(settings):# pragma: no cover
    class ParserImpl:# pragma: no cover
        @staticmethod# pragma: no cover
        def from_crawler(crawler, data):# pragma: no cover
             pass# pragma: no cover
    return ParserImpl# pragma: no cover
load_object = lambda x: mock_parser(x) # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover
from scrapy.settings import Settings # pragma: no cover

crawler = type('MockCrawler', (object,), {'settings': Settings({'ROBOTSTXT_OBEY': False, 'USER_AGENT': 'MockUserAgent', 'ROBOTSTXT_USER_AGENT': 'MockRobotUserAgent', 'ROBOTSTXT_PARSER': 'mock_parser'})})() # pragma: no cover
self = type('Mock', (object,), {'_default_useragent': None, '_robotstxt_useragent': None, 'crawler': None, '_parsers': None, '_parserimpl': None})() # pragma: no cover
self._default_useragent = 'ScrapyBot' # pragma: no cover
self._robotstxt_useragent = 'MyBot' # pragma: no cover
self.crawler = crawler # pragma: no cover
self._parsers = {} # pragma: no cover
self._parserimpl = type('MockParserImpl', (object,), {'from_crawler': staticmethod(lambda crawler, b: None)})() # pragma: no cover

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
