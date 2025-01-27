# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = dynamic_ragged_shape.DynamicRaggedShape.Spec(
    row_partitions=[
        RowPartitionSpec(
            nrows=6,
            nvals=None,
            uniform_row_length=None,
            dtype=dtypes.int64)
    ],
    static_inner_shape=tensor_shape.TensorShape([None]),
    dtype=dtypes.int64)
representation = repr(original)
static_inner_shape = tensor_shape.TensorShape([None])
expected = ('DynamicRaggedShape.Spec(' +
            'row_partitions=(RowPartitionSpec(' +
            'nrows=6, nvals=None, uniform_row_length=None, ' +
            'dtype=tf.int64),), ' +
            f'static_inner_shape={static_inner_shape!r}, ' +
            'dtype=tf.int64)')
self.assertEqual(representation, expected)
