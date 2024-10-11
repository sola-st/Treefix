# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
index = constant_op.constant([0, 1, 2], name='testLayerBroadcasterRepr')
lb = _LayerBroadcaster.from_gather_index(index)
actual = str(lb)
self.assertRegex(actual, '.*Tensor.*, shape=.3... dtype=int32.')
