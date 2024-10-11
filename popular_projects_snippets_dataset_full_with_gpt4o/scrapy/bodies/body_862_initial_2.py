from scrapy import Request # pragma: no cover
from scrapy.spiders import Spider # pragma: no cover
import scrapy.signals # pragma: no cover
from scrapy.crawler import Crawler # pragma: no cover

ScrapyH2Agent = type('ScrapyH2Agent', (object,), {'download_request': lambda self, request, spider: 'Download Request Called'}) # pragma: no cover
self = type('MockSelf', (object,), {'_context_factory': 'context_factory', '_pool': 'pool', '_crawler': Crawler(Spider)})() # pragma: no cover
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
