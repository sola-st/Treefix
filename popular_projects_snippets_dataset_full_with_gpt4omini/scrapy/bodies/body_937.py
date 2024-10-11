# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
self._url = urldefrag(request.url)[0]
# converting to bytes to comply to Twisted interface
self.url = to_bytes(self._url, encoding='ascii')
self.method = to_bytes(request.method, encoding='ascii')
self.body = request.body or None
self.headers = Headers(request.headers)
self.response_headers = None
self.timeout = request.meta.get('download_timeout') or timeout
self.start_time = time()
self.deferred = defer.Deferred().addCallback(self._build_response, request)

# Fixes Twisted 11.1.0+ support as HTTPClientFactory is expected
# to have _disconnectedDeferred. See Twisted r32329.
# As Scrapy implements it's own logic to handle redirects is not
# needed to add the callback _waitForDisconnect.
# Specifically this avoids the AttributeError exception when
# clientConnectionFailed method is called.
self._disconnectedDeferred = defer.Deferred()

self._set_connection_attributes(request)

# set Host header based on url
self.headers.setdefault('Host', self.netloc)

# set Content-Length based len of body
if self.body is not None:
    self.headers['Content-Length'] = len(self.body)
    # just in case a broken http/1.1 decides to keep connection alive
    self.headers.setdefault("Connection", "close")
# Content-Length must be specified in POST method even with no body
elif self.method == b'POST':
    self.headers['Content-Length'] = 0
