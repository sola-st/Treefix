# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
@def_function.function(
    input_signature=[tensor_spec.TensorSpec([3], dtypes.int64)])
def fun(x):
    shape = DynamicRaggedShape([
        RowPartition.from_row_lengths([1, 3], dtype=dtypes.int64),
        RowPartition.from_row_lengths([2, 3, 4, 5], dtype=dtypes.int64)
    ], x)
    result = shape._with_num_row_partitions(3)
    expected = DynamicRaggedShape([
        RowPartition.from_row_lengths([1, 3], dtype=dtypes.int64),
        RowPartition.from_row_lengths([2, 3, 4, 5], dtype=dtypes.int64),
        RowPartition.from_uniform_row_length(
            2, nrows=14, nvals=28, dtype=dtypes.int64)
    ], [14 * 2, 3])
    self.assertShapeEq(expected, result)
fun(constant_op.constant([14, 2, 3], dtype=dtypes.int64))
