# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/matrix_band_part_op_test.py
shape = batch_shape_ + shape_
x = constant_op.constant(np.random.rand(*shape), dtype=dtype_)
with self.session(use_gpu=False):
    for lower in -1, 0, 1, shape_[-2] - 1:
        for upper in -1, 0, 1, shape_[-1] - 1:
            y = array_ops.matrix_band_part(x, lower, upper)
            error = gradient_checker.compute_gradient_error(
                x, x.get_shape().as_list(), y, y.get_shape().as_list())
            self.assertLess(error, 1e-4)
