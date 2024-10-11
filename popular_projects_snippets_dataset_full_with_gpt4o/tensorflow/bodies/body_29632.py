# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
shapes = ((3,), (7, 4))
with self.session():
    for shape in shapes:
        x = constant_op.constant(np.random.rand(*shape), np.float32)
        y = array_ops.matrix_diag(x)
        error = gradient_checker.compute_gradient_error(x,
                                                        x.get_shape().as_list(),
                                                        y,
                                                        y.get_shape().as_list())
        self.assertLess(error, 1e-4)

    # {Sub,super}diagonals/band.
tests = dict()  # tests[shape] = (d_lower, d_upper)
tests[(3,)] = (-1, -1)
tests[(7, 3, 4)] = (-1, 1)
with self.session():
    for shape, diags in tests.items():
        x = constant_op.constant(np.random.rand(*shape), np.float32)
        for align in alignment_list:
            y = array_ops.matrix_diag(x, k=diags, align=align)
            error = gradient_checker.compute_gradient_error(
                x,
                x.get_shape().as_list(), y,
                y.get_shape().as_list())
            self.assertLess(error, 1e-4)
