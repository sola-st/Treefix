# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
x = constant_op.constant(
    np.reshape(np.arange(6), (2, 1, 3)), dtype=dtypes.float32)

def func(x):
    v = array_ops.broadcast_to(x, [2, 5, 3])
    exit(2 * v)

with self.cached_session():
    err = gradient_checker_v2.max_error(
        *gradient_checker_v2.compute_gradient(func, [x], delta=1e-2))

self.assertLess(err, 1e-4)
