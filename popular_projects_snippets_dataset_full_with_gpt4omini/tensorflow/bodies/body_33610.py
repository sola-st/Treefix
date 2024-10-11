# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_square_root_op_test.py
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    tensor = constant_op.constant([[1., 0., -1.], [-1., 1., 0.]])
    self.evaluate(gen_linalg_ops.matrix_square_root(tensor))
