from types import SimpleNamespace # pragma: no cover

self = type('Mock', (object,), {'HTTPClientFactory': None, 'ClientContextFactory': None, '_settings': None, '_crawler': None})() # pragma: no cover
def load_object(path): return path # pragma: no cover
settings = {'DOWNLOADER_HTTPCLIENTFACTORY': 'SomeHttpClientFactory', 'DOWNLOADER_CLIENTCONTEXTFACTORY': 'SomeClientContextFactory'} # pragma: no cover
crawler = SimpleNamespace() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http10.py
from l3.Runtime import _l_
self.HTTPClientFactory = load_object(settings['DOWNLOADER_HTTPCLIENTFACTORY'])
_l_(18330)
self.ClientContextFactory = load_object(settings['DOWNLOADER_CLIENTCONTEXTFACTORY'])
_l_(18331)
self._settings = settings
_l_(18332)
self._crawler = crawler
_l_(18333)
