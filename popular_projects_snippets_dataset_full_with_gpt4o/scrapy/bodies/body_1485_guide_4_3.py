# To ensure the uncaught NotImplementedError path is executed # pragma: no cover
class CustomError(Exception): # pragma: no cover
    pass # pragma: no cover
try: # pragma: no cover
    pass
except CustomError: # pragma: no cover
    print('Handled CustomError') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(16928)
