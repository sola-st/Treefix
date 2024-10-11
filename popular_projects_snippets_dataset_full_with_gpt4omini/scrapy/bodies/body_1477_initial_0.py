class Mock:# pragma: no cover
    def getbool(self, key):# pragma: no cover
        return True# pragma: no cover
    def getlist(self, key):# pragma: no cover
        return [200, 404, 500]# pragma: no cover
# pragma: no cover
settings = Mock() # pragma: no cover
class MockSelf:# pragma: no cover
    pass# pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/httperror.py
from l3.Runtime import _l_
self.handle_httpstatus_all = settings.getbool('HTTPERROR_ALLOW_ALL')
_l_(7733)
self.handle_httpstatus_list = settings.getlist('HTTPERROR_ALLOWED_CODES')
_l_(7734)
