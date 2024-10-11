# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
source_shape = source_shape()
target_shape = target_shape()
layer_broadcasters = layer_broadcasters()
with self.assertRaisesRegex(error_type, error_regex):
    dynamic_ragged_shape._Broadcaster(
        source_shape, target_shape, layer_broadcasters, dtype=dtype)
