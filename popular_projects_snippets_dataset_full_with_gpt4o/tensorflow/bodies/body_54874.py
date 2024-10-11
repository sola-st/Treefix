# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
with self.assertRaisesRegex(TypeError, "must be integer or None"):
    tensor_shape.Dimension(42).merge_with([])

with self.assertRaisesRegex(ValueError, "must be >= 0"):
    tensor_shape.Dimension(42).merge_with(-1)
