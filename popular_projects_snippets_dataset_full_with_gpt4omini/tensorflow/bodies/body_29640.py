# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.session():
    x = constant_op.constant(
        np.random.rand(*input_shape), dtype=dtypes_lib.float32)
    x_diag = constant_op.constant(
        np.random.rand(*diag_shape), dtype=dtypes_lib.float32)

    y = array_ops.matrix_set_diag(x, x_diag, k=diags, align=align)
    error_x = gradient_checker.compute_gradient_error(x,
                                                      x.get_shape().as_list(),
                                                      y,
                                                      y.get_shape().as_list())
    self.assertLess(error_x, 1e-4)
    error_x_diag = gradient_checker.compute_gradient_error(
        x_diag,
        x_diag.get_shape().as_list(), y,
        y.get_shape().as_list())
    self.assertLess(error_x_diag, 1e-4)
