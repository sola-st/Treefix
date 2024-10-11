from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.settings import Settings # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

crawler = type('Mock', (object,), {'settings': Settings({'ROBOTSTXT_OBEY': False, 'USER_AGENT': 'ScrapyBot', 'ROBOTSTXT_USER_AGENT': 'CrawlerBot', 'ROBOTSTXT_PARSER': 'scrapy.robotstxt.RobotParser'})}) # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

class MockSettings:# pragma: no cover
    def getbool(self, key):# pragma: no cover
        return True# pragma: no cover
    def get(self, key, default=None):# pragma: no cover
        if key == 'ROBOTSTXT_PARSER':# pragma: no cover
            return 'mock_parser'# pragma: no cover
        return default# pragma: no cover
# pragma: no cover
crawler = type('MockCrawler', (object,), {'settings': MockSettings()})() # pragma: no cover
self = type('MockSelf', (object,), {'_default_useragent': '', '_robotstxt_useragent': '', 'crawler': None, '_parsers': {}, '_parserimpl': None})() # pragma: no cover
def mock_load_object(path):# pragma: no cover
    class MockParser:# pragma: no cover
        @staticmethod# pragma: no cover
        def from_crawler(crawler, data):# pragma: no cover
            pass# pragma: no cover
    return MockParser# pragma: no cover
# pragma: no cover
load_object = mock_load_object # pragma: no cover

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
