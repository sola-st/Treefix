# Ensuring execution paths are covered and the NotImplementedError is raised # pragma: no cover
class Mock: # pragma: no cover
    def method(self): # pragma: no cover
        pass
mock = Mock() # pragma: no cover
mock.method() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(16928)
