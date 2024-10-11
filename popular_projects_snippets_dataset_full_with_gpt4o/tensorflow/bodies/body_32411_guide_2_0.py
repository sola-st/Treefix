import unittest # pragma: no cover
from unittest import TestCase # pragma: no cover

check_ops = type('MockCheckOps', (object,), { # pragma: no cover
    'assert_proper_iterable': lambda x: (_ for _ in ()).throw(TypeError('to be iterable')) if not hasattr(x, '__iter__') else None # pragma: no cover
})() # pragma: no cover
self = type('MockSelf', (TestCase,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
