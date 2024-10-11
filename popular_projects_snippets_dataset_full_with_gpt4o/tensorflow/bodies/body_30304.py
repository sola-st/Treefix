# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/identity_op_py_test.py
with self.cached_session():
    shape = [2, 3]
    array_2x3 = [[1, 2, 3], [6, 5, 4]]
    tensor = constant_op.constant(array_2x3)
    self.assertEqual(shape, tensor.get_shape())
    self.assertEqual(shape, array_ops.identity(tensor).get_shape())
    self.assertEqual(shape, array_ops.identity(array_2x3).get_shape())
    self.assertEqual(shape,
                     array_ops.identity(np.array(array_2x3)).get_shape())
