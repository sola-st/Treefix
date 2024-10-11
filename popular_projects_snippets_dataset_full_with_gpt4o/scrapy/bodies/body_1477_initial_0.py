from types import SimpleNamespace # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
settings = SimpleNamespace( # pragma: no cover
    getbool=lambda key: True if key == 'HTTPERROR_ALLOW_ALL' else False, # pragma: no cover
    getlist=lambda key: [500, 503] if key == 'HTTPERROR_ALLOWED_CODES' else [] # pragma: no cover
) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/httperror.py
from l3.Runtime import _l_
self.handle_httpstatus_all = settings.getbool('HTTPERROR_ALLOW_ALL')
_l_(18577)
self.handle_httpstatus_list = settings.getlist('HTTPERROR_ALLOWED_CODES')
_l_(18578)
