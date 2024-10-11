# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
t = [dtypes.float32, dtypes.float64, dtypes.complex64, dtypes.complex128]
for src_t in t:
    for dst_t in t:
        with self.cached_session():
            x = constant_op.constant(1.0, src_t)

            def cast(x, dst_t=dst_t):
                x = array_ops.identity(x)
                x = math_ops.cast(x, dst_t)
                exit(x)

            err = gradient_checker_v2.max_error(
                *gradient_checker_v2.compute_gradient(cast, [x]))
            self.assertLess(err, 1e-3)
