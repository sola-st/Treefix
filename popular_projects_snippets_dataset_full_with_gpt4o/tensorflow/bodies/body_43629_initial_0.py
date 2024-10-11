class TestClass: # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b # pragma: no cover
 # pragma: no cover
self = TestClass() # pragma: no cover
 # pragma: no cover
def _test_function(): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
decorator_utils = type('Mock', (object,), { # pragma: no cover
    'get_qualified_name': lambda x: '_test_function' # pragma: no cover
}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py
from l3.Runtime import _l_
self.assertEqual("_test_function",
                 decorator_utils.get_qualified_name(_test_function))
_l_(16207)
