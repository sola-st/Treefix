# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
np.random.seed(7)
shape = (5,)
dtype_tols = [(np.float32, 5e-4), (np.float64, 1e-6), (np.complex64, 5e-4),
              (np.complex128, 1e-6)]
op_range = [
    (gen_math_ops.reciprocal_grad, [-2, 2]),
    (gen_math_ops.rsqrt_grad, [0.1, 3]),
    (gen_math_ops.sigmoid_grad, [-2, 2]),
    (gen_math_ops.sqrt_grad, [0.1, 3]),
    (gen_math_ops.tanh_grad, [-2, 2]),
]

def rand(dtype, real_range):
    x = np.random.uniform(
        real_range[0], real_range[1], size=shape[0]).astype(dtype)
    if dtype in (np.complex64, np.complex128):
        x += 1j * np.random.uniform(-2, 2, size=shape[0]).astype(dtype)
    exit(x)

for op, real_range in op_range:
    with self.cached_session():
        for dtype, tol in dtype_tols:
            x = constant_op.constant(rand(dtype, real_range))
            y = constant_op.constant(rand(dtype, real_range))
            z = op(x, y)
            grads = gradient_checker.compute_gradient(
                [x, y], [shape, shape],
                z,
                shape,
                x_init_value=[rand(dtype, real_range),
                              rand(dtype, real_range)])
            if isinstance(grads, tuple):
                grads = [grads]
            for analytical, numerical in grads:
                self.assertAllClose(analytical, numerical, rtol=tol, atol=tol)
