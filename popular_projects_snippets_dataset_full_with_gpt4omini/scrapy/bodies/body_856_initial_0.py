from scrapy.utils.project import get_project_settings # pragma: no cover
from scrapy.http import HtmlResponse # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.HTTPClientFactory = None # pragma: no cover
self.ClientContextFactory = None # pragma: no cover
settings = {'DOWNLOADER_HTTPCLIENTFACTORY': 'path.to.httpclientfactory', 'DOWNLOADER_CLIENTCONTEXTFACTORY': 'path.to.clientcontextfactory'} # pragma: no cover
crawler = None # pragma: no cover
load_object = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http10.py
from l3.Runtime import _l_
self.HTTPClientFactory = load_object(settings['DOWNLOADER_HTTPCLIENTFACTORY'])
_l_(7427)
self.ClientContextFactory = load_object(settings['DOWNLOADER_CLIENTCONTEXTFACTORY'])
_l_(7428)
self._settings = settings
_l_(7429)
self._crawler = crawler
_l_(7430)
