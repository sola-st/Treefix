from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

class MockSettings: # pragma: no cover
    def getbool(self, key): # pragma: no cover
        if key == 'ROBOTSTXT_OBEY': # pragma: no cover
            return False # pragma: no cover
        return True # pragma: no cover
    def get(self, key, default=None): # pragma: no cover
        if key == 'USER_AGENT': # pragma: no cover
            return 'MockUserAgent' # pragma: no cover
        elif key == 'ROBOTSTXT_PARSER': # pragma: no cover
            return 'MockParser' # pragma: no cover
        return default # pragma: no cover
 # pragma: no cover
class MockCrawler: # pragma: no cover
    settings = MockSettings() # pragma: no cover
 # pragma: no cover
class MockParser: # pragma: no cover
    @staticmethod # pragma: no cover
    def from_crawler(crawler, data): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
def load_object(path): # pragma: no cover
    if path == 'MockParser': # pragma: no cover
        return MockParser # pragma: no cover
 # pragma: no cover
crawler = MockCrawler() # pragma: no cover
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
