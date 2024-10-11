# Extracted from ./data/repos/scrapy/scrapy/core/http2/agent.py
self._connections.pop(key)

# Call the errback of all the pending requests for this connection
pending_requests = self._pending_requests.pop(key, None)
while pending_requests:
    d = pending_requests.popleft()
    d.errback(errors)
