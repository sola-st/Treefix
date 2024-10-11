import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock(spec=[]) # pragma: no cover
def assertRaisesRegex(exception, regex): pass # pragma: no cover
self.assertRaisesRegex = assertRaisesRegex # pragma: no cover
class CheckOps: # pragma: no cover
    def assert_proper_iterable(self, item): # pragma: no cover
        if not hasattr(item, '__iter__'): raise TypeError('Expected object to be iterable') # pragma: no cover
check_ops = CheckOps() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
