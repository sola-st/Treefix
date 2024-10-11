# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py

@def_function.function
def dynamic_shape_sparse(dense_shape):
    ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2], [3, 3]])
    val = np.array([0, 10, 13, 14, 32, 33])
    sp = sparse_tensor.SparseTensor(
        constant_op.constant(ind, dtypes.int64),
        constant_op.constant(val, dtypes.int64),
        dense_shape)

    sp.set_shape(tensor_shape.TensorShape(None))
    self.assertEqual(sp.shape, tensor_shape.TensorShape(None))

    sp.set_shape(tensor_shape.TensorShape([None, None]))
    self.assertEqual(sp.shape, tensor_shape.TensorShape([None, None]))

    sp.set_shape(tensor_shape.TensorShape([5, None]))
    self.assertEqual(sp.shape, tensor_shape.TensorShape([5, None]))

    sp.set_shape(tensor_shape.TensorShape([None, 6]))
    self.assertEqual(sp.shape, tensor_shape.TensorShape([5, 6]))

    sp.set_shape(tensor_shape.TensorShape([None, None]))
    self.assertEqual(sp.shape, tensor_shape.TensorShape([5, 6]))

    sp.set_shape(tensor_shape.TensorShape([5, 6]))
    self.assertEqual(sp.shape, tensor_shape.TensorShape([5, 6]))

    with self.assertRaises(ValueError):
        sp.set_shape([None, None, None])

    with self.assertRaises(ValueError):
        sp.set_shape([3, None])

    with self.assertRaises(ValueError):
        sp.set_shape([None, 7])

    with self.assertRaises(ValueError):
        sp.set_shape([3, 6])

dense_shape_spec = tensor_spec.TensorSpec(None, dtypes.int64)
_ = dynamic_shape_sparse.get_concrete_function(dense_shape_spec)
