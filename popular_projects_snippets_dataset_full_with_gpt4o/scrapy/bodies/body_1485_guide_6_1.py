# The following code initializes the underlying structure to handle the uncovered path # pragma: no cover
def uncovered_path(): # pragma: no cover
    try: # pragma: no cover
        raise NotImplementedError() # pragma: no cover
    except NotImplementedError: # pragma: no cover
        print('NotImplementedError was raised and handled successfully') # pragma: no cover
uncovered_path() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(16928)
