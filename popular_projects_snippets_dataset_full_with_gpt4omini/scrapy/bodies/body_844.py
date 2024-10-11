# Extracted from ./data/repos/scrapy/scrapy/core/http2/agent.py
super().__init__(
    reactor=reactor,
    pool=pool,
    context_factory=context_factory,
    connect_timeout=connect_timeout,
    bind_address=bind_address,
)
self._proxy_uri = proxy_uri
