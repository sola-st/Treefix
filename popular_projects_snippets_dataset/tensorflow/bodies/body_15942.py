# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
spec = DynamicRaggedShape.Spec(
    row_partitions=[
        RowPartitionSpec(
            nrows=3, nvals=7, uniform_row_length=None, dtype=dtypes.int32),
        RowPartitionSpec(
            nrows=7,
            nvals=None,
            uniform_row_length=None,
            dtype=dtypes.int32)
    ],
    static_inner_shape=tensor_shape.TensorShape(None),
    dtype=dtypes.int32)
expected = DynamicRaggedShape.Spec(
    row_partitions=[
        RowPartitionSpec(
            nrows=3, nvals=7, uniform_row_length=None, dtype=dtypes.int32),
        RowPartitionSpec(
            nrows=7,
            nvals=None,
            uniform_row_length=None,
            dtype=dtypes.int32)
    ],
    static_inner_shape=tensor_shape.TensorShape([None, None]),
    dtype=dtypes.int32)
actual = spec._truncate(4)
self.assertDynamicRaggedShapeSpecEqual(actual, expected)
