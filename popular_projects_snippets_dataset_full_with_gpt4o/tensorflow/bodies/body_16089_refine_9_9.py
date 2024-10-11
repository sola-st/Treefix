self = type('Mock', (object,), {'assertAllEqual': lambda self, a, b: None})() # pragma: no cover

import numpy as np # pragma: no cover

self = type('Mock', (object,), {'assertAllEqual': lambda self, a, b: np.testing.assert_array_equal(a.numpy(), b)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tile_op_test.py
# When the input is a `Tensor`, ragged_tile just delegates to tf.tile.
from l3.Runtime import _l_
dt = constant_op.constant([[1, 2], [3, 4]])
_l_(22240)
tiled = ragged_array_ops.tile(dt, [3, 2])
_l_(22241)
expected = [[1, 2, 1, 2], [3, 4, 3, 4],
            [1, 2, 1, 2], [3, 4, 3, 4],
            [1, 2, 1, 2], [3, 4, 3, 4]]  # pyformat: disable
_l_(22242)  # pyformat: disable
self.assertAllEqual(tiled, expected)
_l_(22243)
