import unittest # pragma: no cover

class MockTest(unittest.TestCase): # pragma: no cover
    def test_non_iterable(self): # pragma: no cover
        non_iterable = 1234 # pragma: no cover
        with self.assertRaisesRegex(TypeError, 'to be iterable'): # pragma: no cover
            check_ops.assert_proper_iterable(non_iterable) # pragma: no cover
 # pragma: no cover
self = MockTest('test_non_iterable') # pragma: no cover
self.setUp() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
