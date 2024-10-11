from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.project import get_project_settings # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

crawler = type('Mock', (object,), {'settings': get_project_settings()})() # pragma: no cover
self = type('Mock', (object,), {'_default_useragent': '', '_robotstxt_useragent': '', 'crawler': None, '_parsers': [], '_parserimpl': None})() # pragma: no cover
load_object = lambda path: type('MockParser', (object,), {'from_crawler': lambda cls, crawler, content: None}) # pragma: no cover

from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.utils.project import get_project_settings # pragma: no cover
from scrapy.utils.misc import load_object # pragma: no cover

class MockSettings: # pragma: no cover
    def getbool(self, name): # pragma: no cover
        if name == 'ROBOTSTXT_OBEY': # pragma: no cover
            return True  # Change this to False if you want to raise NotConfigured # pragma: no cover
        return False # pragma: no cover
    def get(self, name, default=None): # pragma: no cover
        settings = { # pragma: no cover
            'USER_AGENT': 'Mozilla/5.0', # pragma: no cover
            'ROBOTSTXT_USER_AGENT': None, # pragma: no cover
            'ROBOTSTXT_PARSER': 'path.to.MockParser' # pragma: no cover
        } # pragma: no cover
        return settings.get(name, default) # pragma: no cover
 # pragma: no cover
crawler = type('Mock', (object,), {'settings': MockSettings()})() # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._default_useragent = '' # pragma: no cover
        self._robotstxt_useragent = '' # pragma: no cover
        self.crawler = None # pragma: no cover
        self._parsers = {} # pragma: no cover
        self._parserimpl = None # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
self.crawler = crawler # pragma: no cover
self._default_useragent = 'Scrapy' # pragma: no cover
self._robotstxt_useragent = None # pragma: no cover
 # pragma: no cover
class MockParser: # pragma: no cover
    @classmethod # pragma: no cover
    def from_crawler(cls, crawler, content): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
load_object = lambda path: MockParser # pragma: no cover

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
