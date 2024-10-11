import numpy as np # pragma: no cover

self = type('MockSelf', (), {'evaluate': lambda self, x: x})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
x = array_ops.ones([1, 2, 3, 2], name="x")
_l_(7735)
y = array_ops.ones([2, 3, 3], name="y")
_l_(7736)
a1 = check_ops.assert_shapes([
    (x, (Ellipsis, "N", "Q")),
    (y, (Ellipsis, "N", "D")),
])
_l_(7737)
a2 = check_ops.assert_shapes([
    (x, "*NQ"),
    (y, "*ND"),
])
_l_(7738)
with ops.control_dependencies([a1, a2]):
    _l_(7740)

    out = array_ops.identity(x)
    _l_(7739)
self.evaluate(out)
_l_(7741)
