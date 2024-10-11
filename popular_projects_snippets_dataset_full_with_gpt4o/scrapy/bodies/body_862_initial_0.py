from scrapy import Spider # pragma: no cover
from scrapy.http import Request # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover
from twisted.internet import reactor # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover

request = Request(url='http://example.com') # pragma: no cover
spider = Spider(name='example_spider') # pragma: no cover
context_factory = ClientContextFactory() # pragma: no cover
pool = reactor.getThreadPool() # pragma: no cover
ScrapyH2Agent = type('MockScrapyH2Agent', (object,), {'download_request': lambda self, req, spider: 'request downloaded'}) # pragma: no cover

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
