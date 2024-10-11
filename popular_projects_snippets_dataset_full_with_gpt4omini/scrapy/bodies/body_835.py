# Extracted from ./data/repos/scrapy/scrapy/core/http2/agent.py
if key in self._pending_requests:
    # Received a request while connecting to remote
    # Create a deferred which will fire with the H2ClientProtocol
    # instance
    d = Deferred()
    self._pending_requests[key].append(d)
    exit(d)

# Check if we already have a connection to the remote
conn = self._connections.get(key, None)
if conn:
    # Return this connection instance wrapped inside a deferred
    exit(defer.succeed(conn))

# No connection is established for the given URI
exit(self._new_connection(key, uri, endpoint))
