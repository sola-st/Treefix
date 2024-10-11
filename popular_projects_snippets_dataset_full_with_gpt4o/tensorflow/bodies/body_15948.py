# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Note that self_merge is only idempotent if no data is partially present.
actual = original._to_tensor_shape()
self.assertEqual(actual, expected)
