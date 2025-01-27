# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths([2, (1, 2)])
with self.assertRaisesRegex(TypeError, 'index should be an int'):
    # This error is not exposed directly to the end user.
    original._dimension(0.5)
