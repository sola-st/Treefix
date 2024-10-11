class MockFile:# pragma: no cover
    def close(self):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
file = MockFile() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
from l3.Runtime import _l_
file.close()
_l_(9715)
