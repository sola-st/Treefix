from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover
class MockCrawler: # pragma: no cover
    def __init__(self, settings): # pragma: no cover
        self.settings = settings # pragma: no cover
class MockSettings: # pragma: no cover
    def __init__(self, obey_robots, user_agent, robots_user_agent, parser): # pragma: no cover
        self.obey_robots = obey_robots # pragma: no cover
        self.user_agent = user_agent # pragma: no cover
        self.robots_user_agent = robots_user_agent # pragma: no cover
        self.parser = parser # pragma: no cover
    def getbool(self, name): # pragma: no cover
        return self.obey_robots if name == 'ROBOTSTXT_OBEY' else None # pragma: no cover
    def get(self, name, default=None): # pragma: no cover
        if name == 'USER_AGENT': # pragma: no cover
            return self.user_agent or default # pragma: no cover
        elif name == 'ROBOTSTXT_USER_AGENT': # pragma: no cover
            return self.robots_user_agent or default # pragma: no cover
        elif name == 'ROBOTSTXT_PARSER': # pragma: no cover
            return self.parser or default # pragma: no cover
        else: # pragma: no cover
            return default # pragma: no cover
MockParser = type('MockParser', (object,), {'from_crawler': staticmethod(lambda crawler, data: data)}) # pragma: no cover

crawler = MockCrawler(MockSettings(False, 'ScrapyUserAgent', None, 'MockParser')) # pragma: no cover

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
