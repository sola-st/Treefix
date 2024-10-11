from scrapy.http import Request # pragma: no cover

class MockContextFactory: pass # pragma: no cover
class MockPool: pass # pragma: no cover
class MockCrawler: pass # pragma: no cover
self = type('Mock', (object,), {'_context_factory': MockContextFactory(), '_pool': MockPool(), '_crawler': MockCrawler()})() # pragma: no cover
request = Request(url='http://example.com') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http2.py
from l3.Runtime import _l_
agent = ScrapyH2Agent(
    context_factory=self._context_factory,
    pool=self._pool,
    crawler=self._crawler,
)
_l_(7370)
aux = agent.download_request(request, spider)
_l_(7371)
exit(aux)
