# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = DynamicRaggedShape([RowPartition.from_row_lengths([3, 3])],
                       inner_shape)
actual = a._to_tensor_shape()
self.assertDimsEqual(
    tensor_shape.TensorShape(None), actual)
