# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = DynamicRaggedShape.from_lengths([2, (1, 2), 3])
actual = a._to_tensor_shape()
self.assertDimsEqual(tensor_shape.TensorShape([2, None, 3]), actual)
