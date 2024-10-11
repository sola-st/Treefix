from scrapy.exceptions import NotConfigured # pragma: no cover
from unittest.mock import Mock # pragma: no cover

crawler = Mock() # pragma: no cover
crawler.settings = Mock() # pragma: no cover
crawler.settings.getbool = Mock(return_value=True) # pragma: no cover
crawler.settings.get = Mock(side_effect=lambda k, d=None: d) # pragma: no cover
self = Mock() # pragma: no cover
load_object = Mock(return_value=Mock()) # pragma: no cover

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
