def example_function(): # pragma: no cover
    raise NotImplementedError() # pragma: no cover
 # pragma: no cover
try: # pragma: no cover
    example_function() # pragma: no cover
except NotImplementedError: # pragma: no cover
    print('NotImplementedError was raised as expected') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(16928)
