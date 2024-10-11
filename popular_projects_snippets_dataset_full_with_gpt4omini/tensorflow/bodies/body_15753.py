# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
assert isinstance(x, dynamic_ragged_shape._Broadcaster)
assert isinstance(y, dynamic_ragged_shape._Broadcaster)
self.assertShapeEq(x.source_shape, y.source_shape)
self.assertShapeEq(x.target_shape, y.target_shape)
self.assertLen(x._layer_broadcasters, len(y._layer_broadcasters))
for x_layer, y_layer in zip(x._layer_broadcasters, y._layer_broadcasters):
    self.assertLayerBroadcasterEq(x_layer, y_layer)
