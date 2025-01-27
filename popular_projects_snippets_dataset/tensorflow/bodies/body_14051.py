# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
x = constant_op.constant([1, 2, 3, 4])
y = constant_op.constant([[1, 2], [3, 4], [5, 6], [7, 8]])
fields = {"x": x, "y": y}
nrows = constant_op.constant(4)
shape = tensor_shape.TensorShape((4,))
row_partitions = ()
rs = structured_tensor_dynamic._dynamic_ragged_shape_init(
    fields, shape, nrows, row_partitions)
self.assertEqual(
    repr(rs._to_tensor_shape()), repr(tensor_shape.TensorShape((4,))))
