from scrapy.http import Request # pragma: no cover
from unittest.mock import Mock # pragma: no cover

ScrapyH2Agent = Mock() # pragma: no cover
self = Mock() # pragma: no cover
self._context_factory = Mock() # pragma: no cover
self._pool = Mock() # pragma: no cover
self._crawler = Mock() # pragma: no cover
request = Request(url='http://example.com', callback=lambda response: None) # pragma: no cover
spider = Mock() # pragma: no cover

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
