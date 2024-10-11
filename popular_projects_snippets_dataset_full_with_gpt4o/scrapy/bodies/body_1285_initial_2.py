from unittest.mock import Mock # pragma: no cover

crawler = Mock(settings={'some_setting': 'some_value'}) # pragma: no cover
cls = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/redirect.py
from l3.Runtime import _l_
aux = cls(crawler.settings)
_l_(20930)
exit(aux)
