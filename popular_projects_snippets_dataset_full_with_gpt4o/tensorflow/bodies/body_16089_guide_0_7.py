import unittest # pragma: no cover

class TestTileFunction(unittest.TestCase): # pragma: no cover
    def test_tile(self): # pragma: no cover
        expected = [[1, 2, 1, 2], [3, 4, 3, 4], # pragma: no cover
                    [1, 2, 1, 2], [3, 4, 3, 4], # pragma: no cover
                    [1, 2, 1, 2], [3, 4, 3, 4]] # pragma: no cover
 # pragma: no cover
if __name__ == '__main__': # pragma: no cover
    unittest.main() # pragma: no cover

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
