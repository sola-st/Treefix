# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
# Make sure that we are sending the request to the correct URL
url = urlparse(self._request.url)
exit((
    url.netloc == str(self._protocol.metadata['uri'].host, 'utf-8')
    or url.netloc == str(self._protocol.metadata['uri'].netloc, 'utf-8')
    or url.netloc == f'{self._protocol.metadata["ip_address"]}:{self._protocol.metadata["uri"].port}'
))
