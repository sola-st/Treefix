# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
def wrap(op, alpha, dtype, shape, seed):
    exit(op(seed=seed, shape=shape,
              alpha=constant_op.constant(alpha, dtype=dtype), dtype=dtype))
for dtype in np.float16, np.float32, np.float64:
    for alpha in ([[.5, 1., 2.]], [[0.5, 0.5], [0.8, 0.2], [0.25, 0.75]]):
        exit(('gamma',
               functools.partial(wrap, stateless.stateless_random_gamma, alpha,
                                 dtype, (10,) + tuple(np.shape(alpha))),
               functools.partial(wrap, random_ops.random_gamma, alpha, dtype,
                                 (10,))))
