# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(
    ValueError, r'dtype of .* is .*int64.*: expected .*int32.*'):
    DynamicRaggedShape.Spec(
        row_partitions=[
            RowPartitionSpec(
                nrows=None,
                nvals=None,
                uniform_row_length=None,
                dtype=dtypes.int32),
            RowPartitionSpec(
                nrows=None,
                nvals=None,
                uniform_row_length=None,
                dtype=dtypes.int64)
        ],
        static_inner_shape=tensor_shape.TensorShape(None),
        dtype=dtypes.int32)
