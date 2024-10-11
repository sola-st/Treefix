class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover

import unittest # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
from l3.Runtime import _l_
x = constant_op.constant(1.0)
_l_(10147)
y = constant_op.constant(1.0)
_l_(10148)
with backprop.GradientTape() as g:
    _l_(10151)

    g.watch([x, y])
    _l_(10149)
    z = y * 2
    _l_(10150)
with self.assertRaisesRegex(
    ValueError, "Unknown value for unconnected_gradients: 'nonsense'"):
    _l_(10153)

    g.gradient(z, x, unconnected_gradients='nonsense')
    _l_(10152)
