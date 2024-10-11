class Mock:  # pragma: no cover
    def assertAllEqual(self, a, b):  # pragma: no cover
        assert (a == b).all()  # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tile_op_test.py
# When the input is a `Tensor`, ragged_tile just delegates to tf.tile.
from l3.Runtime import _l_
dt = constant_op.constant([[1, 2], [3, 4]])
_l_(9863)
tiled = ragged_array_ops.tile(dt, [3, 2])
_l_(9864)
expected = [[1, 2, 1, 2], [3, 4, 3, 4],
            [1, 2, 1, 2], [3, 4, 3, 4],
            [1, 2, 1, 2], [3, 4, 3, 4]]  # pyformat: disable
_l_(9865)  # pyformat: disable
self.assertAllEqual(tiled, expected)
_l_(9866)
