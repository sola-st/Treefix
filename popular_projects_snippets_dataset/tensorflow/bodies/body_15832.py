# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
shape_a = DynamicRaggedShape.from_lengths(lengths_a)
result = tensor_util.constant_value(shape_a[dim])
self.assertEqual(result, expected)
