# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
x = ragged_factory_ops.constant_value([[1, 2, 3], [4]])
fields = {"x": x}
nrows = constant_op.constant(2, dtype=dtypes.int64)
shape = tensor_shape.TensorShape([2, None])
row_partitions = tuple(x._nested_row_partitions)
rs = structured_tensor_dynamic._dynamic_ragged_shape_init(
    fields, shape, nrows, row_partitions)
self.assertEqual(
    repr(rs._to_tensor_shape()), repr(tensor_shape.TensorShape((2, None))))
