# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
np.random.seed(0)
shapes = ((3,), (3, 3), (3, 3, 3))
dtypes = (dtypes_lib.float32, dtypes_lib.float64)
with self.session(use_gpu=False):
    errors = []
    for shape in shapes:
        for dtype in dtypes:
            x1 = constant_op.constant(np.random.rand(*shape), dtype=dtype)
            y = array_ops.diag(x1)
            error = gradient_checker.compute_gradient_error(
                x1,
                x1.get_shape().as_list(), y,
                y.get_shape().as_list())
            tf_logging.info("error = %f", error)
            self.assertLess(error, 1e-4)
