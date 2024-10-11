from scrapy import Request, Spider # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover
from twisted.internet import reactor # pragma: no cover
from twisted.web.client import HTTPConnectionPool # pragma: no cover

ScrapyH2Agent = type('ScrapyH2Agent', (object,), {'__init__': lambda self, context_factory, pool, crawler: None, 'download_request': lambda self, request, spider: 'request_downloaded'}) # pragma: no cover
self = type('Mock', (object,), {'_context_factory': ClientContextFactory(), '_pool': HTTPConnectionPool(reactor), '_crawler': Crawler(Spider)})() # pragma: no cover
request = Request(url='http://example.com') # pragma: no cover
spider = Spider(name='example_spider') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http2.py
from l3.Runtime import _l_
agent = ScrapyH2Agent(
    context_factory=self._context_factory,
    pool=self._pool,
    crawler=self._crawler,
)
_l_(18274)
aux = agent.download_request(request, spider)
_l_(18275)
exit(aux)
