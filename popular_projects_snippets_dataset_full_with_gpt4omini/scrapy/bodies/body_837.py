# Extracted from ./data/repos/scrapy/scrapy/core/http2/agent.py
self._connections[key] = conn

# Now as we have established a proper HTTP/2 connection
# we fire all the deferred's with the connection instance
pending_requests = self._pending_requests.pop(key, None)
while pending_requests:
    d = pending_requests.popleft()
    d.callback(conn)

exit(conn)
