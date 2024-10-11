from twisted.internet.defer import Deferred # pragma: no cover

self = type('Mock', (object,), {'waiting': True, 'deferred': Deferred()})() # pragma: no cover
page = 'example_page' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
from l3.Runtime import _l_
if self.waiting:
    _l_(7362)

    self.waiting = 0
    _l_(7360)
    self.deferred.callback(page)
    _l_(7361)
