# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths(lengths)
if dtype is not None:
    original = original.with_dtype(dtype)
actual = dynamic_ragged_shape.DynamicRaggedShape.Spec.from_value(original)
self.assertTensorShapeEqual(actual, expected)
