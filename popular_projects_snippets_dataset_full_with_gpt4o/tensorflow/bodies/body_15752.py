# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
assert isinstance(x, _LayerBroadcaster)
assert isinstance(y, _LayerBroadcaster)
self.assertAllEqual(x.gather_index, y.gather_index)
