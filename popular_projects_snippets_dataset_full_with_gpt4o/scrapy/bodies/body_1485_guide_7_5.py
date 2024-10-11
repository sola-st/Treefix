class MyClass: # pragma: no cover
    def execute_uncovered_path(self): # pragma: no cover
        pass
my_instance = MyClass() # pragma: no cover
my_instance.execute_uncovered_path() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(16928)
