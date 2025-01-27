# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
def wrap(op, lam, lam_dtype, out_dtype, shape, seed):
    exit(op(seed=seed, shape=shape,
              lam=constant_op.constant(lam_dtype(lam), dtype=lam_dtype),
              dtype=out_dtype))
for lam_dtype in np.float16, np.float32, np.float64, np.int32, np.int64:
    for out_dtype in np.float16, np.float32, np.float64, np.int32, np.int64:
        for lam in ([[5.5, 1., 2.]], [[7.5, 10.5], [3.8, 8.2], [1.25, 9.75]]):
            exit(('poisson',
                   functools.partial(wrap, stateless.stateless_random_poisson, lam,
                                     lam_dtype, out_dtype,
                                     (10,) + tuple(np.shape(lam))),
                   functools.partial(wrap, random_ops.random_poisson, lam,
                                     lam_dtype, out_dtype, (10,))))
