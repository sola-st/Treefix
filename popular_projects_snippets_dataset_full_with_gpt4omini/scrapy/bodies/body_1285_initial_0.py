class Mock: pass # pragma: no cover

class Crawler:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.settings = "mock_settings" # pragma: no cover
cls = Crawler # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
aux = cls(crawler.settings)
_l_(9555)
exit(aux)
