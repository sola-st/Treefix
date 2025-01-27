# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths([2, (3, 5), 6],
                                           dtype=dtypes.int64)
spec = DynamicRaggedShape.Spec(
    row_partitions=[
        RowPartitionSpec(nrows=2,
                         nvals=8,
                         dtype=dtypes.int64)
    ],
    static_inner_shape=tensor_shape.TensorShape([8, 6]),
    dtype=dtypes.int64)
result = original._merge_with_spec(spec)
self.assertShapeEq(result, original)
