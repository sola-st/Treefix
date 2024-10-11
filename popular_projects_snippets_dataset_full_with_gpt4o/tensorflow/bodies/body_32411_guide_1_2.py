import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

check_ops = Mock() # pragma: no cover
def assert_proper_iterable(value): # pragma: no cover
    if not hasattr(value, '__iter__'): raise TypeError('Expected object to be iterable') # pragma: no cover
check_ops.assert_proper_iterable = assert_proper_iterable # pragma: no cover
self = Mock() # pragma: no cover
self.assertRaisesRegex = unittest.TestCase().assertRaisesRegex # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
