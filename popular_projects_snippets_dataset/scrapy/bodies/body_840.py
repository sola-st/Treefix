# Extracted from ./data/repos/scrapy/scrapy/core/http2/agent.py
self._reactor = reactor
self._pool = pool
self._context_factory = AcceptableProtocolsContextFactory(context_factory, acceptable_protocols=[b'h2'])
self.endpoint_factory = _StandardEndpointFactory(
    self._reactor, self._context_factory, connect_timeout, bind_address
)
