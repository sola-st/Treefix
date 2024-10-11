# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/identity_n_op_py_test.py
with self.cached_session():
    shape = [2, 3]
    array_2x3 = [[1, 2, 3], [6, 5, 4]]
    tensor = constant_op.constant(array_2x3)
    self.assertEqual(shape, tensor.get_shape())
    self.assertEqual(shape, array_ops.identity_n([tensor])[0].get_shape())
    self.assertEqual(shape, array_ops.identity_n([array_2x3])[0].get_shape())
