# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a_0 = constant_op.constant(1, dtypes.int64)
b_0 = constant_op.constant(3, dtypes.int64)
[a_layer, b_layer
] = dynamic_ragged_shape._broadcast_dynamic_shape_first_layer(a_0, b_0)
expected_a_layer = _LayerBroadcaster.from_gather_index([0, 0, 0])
expected_b_layer = _LayerBroadcaster.from_gather_index([0, 1, 2])
self.assertLayerBroadcasterEq(expected_a_layer, a_layer)
self.assertLayerBroadcasterEq(expected_b_layer, b_layer)
