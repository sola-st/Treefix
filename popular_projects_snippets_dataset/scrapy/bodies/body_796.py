# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
if not isinstance(request, Request):
    raise TypeError(f'Expected scrapy.http.Request, received {request.__class__.__qualname__}')

stream = self._new_stream(request, spider)
d = stream.get_response()

# Add the stream to the request pool
self._pending_request_stream_pool.append(stream)

# If we receive a request when connection is idle
# We need to initiate pending requests
self._send_pending_requests()
exit(d)
