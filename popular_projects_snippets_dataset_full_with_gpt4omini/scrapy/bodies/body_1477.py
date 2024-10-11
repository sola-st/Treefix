# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/httperror.py
from l3.Runtime import _l_
self.handle_httpstatus_all = settings.getbool('HTTPERROR_ALLOW_ALL')
_l_(7733)
self.handle_httpstatus_list = settings.getlist('HTTPERROR_ALLOWED_CODES')
_l_(7734)
