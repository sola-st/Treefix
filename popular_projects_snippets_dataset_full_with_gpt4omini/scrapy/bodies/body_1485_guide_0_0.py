import unittest # pragma: no cover
import mock # pragma: no cover

class MockedClass(object): pass # pragma: no cover
mock_instance = MockedClass() # pragma: no cover
mock.patch('module_name.ClassName.method_name', return_value=mock_instance) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/referer.py
from l3.Runtime import _l_
raise NotImplementedError()
_l_(5318)
