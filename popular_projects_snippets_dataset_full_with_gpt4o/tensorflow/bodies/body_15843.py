# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths(
    [2, (4, 4), 6], dtype=dtypes.int64)
spec = DynamicRaggedShape.Spec._from_tensor_shape(
    tensor_shape.TensorShape([2, 4, 6]),
    num_row_partitions=0,
    dtype=dtypes.int64)
result = original._merge_with_spec(spec)
original = DynamicRaggedShape.from_lengths([2, 4, 6],
                                           num_row_partitions=1,
                                           dtype=dtypes.int64)
self.assertShapeEq(result, original)
