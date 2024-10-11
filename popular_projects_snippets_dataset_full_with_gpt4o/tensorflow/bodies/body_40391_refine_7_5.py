from unittest import TestCase # pragma: no cover

self = type('Mock', (TestCase,), {'assertRaisesRegex': TestCase.assertRaisesRegex})() # pragma: no cover

import unittest # pragma: no cover

self = type('Mock', (object,), {'assertRaisesRegex': unittest.TestCase().assertRaisesRegex})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
from l3.Runtime import _l_
x = constant_op.constant(1.0)
_l_(22428)
y = constant_op.constant(1.0)
_l_(22429)
with backprop.GradientTape() as g:
    _l_(22432)

    g.watch([x, y])
    _l_(22430)
    z = y * 2
    _l_(22431)
with self.assertRaisesRegex(
    ValueError, "Unknown value for unconnected_gradients: 'nonsense'"):
    _l_(22434)

    g.gradient(z, x, unconnected_gradients='nonsense')
    _l_(22433)
