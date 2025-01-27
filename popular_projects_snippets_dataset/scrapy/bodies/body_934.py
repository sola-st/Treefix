# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
self.transport.loseConnection()

# transport cleanup needed for HTTPS connections
if self.factory.url.startswith(b'https'):
    self.transport.stopProducing()

self.factory.noPage(
    defer.TimeoutError(f"Getting {self.factory.url} took longer "
                       f"than {self.factory.timeout} seconds."))
