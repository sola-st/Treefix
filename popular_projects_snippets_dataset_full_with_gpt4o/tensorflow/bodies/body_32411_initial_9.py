import unittest # pragma: no cover

self = unittest.TestCase() # pragma: no cover
check_ops = type('Mock', (object,), {'assert_proper_iterable': lambda x: (x if hasattr(x, '__iter__') else (_ for _ in ()).throw(TypeError('Non-iterables are not allowed')))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
