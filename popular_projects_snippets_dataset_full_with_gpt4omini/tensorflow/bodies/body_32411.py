# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(9853)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(9855)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(9854)
