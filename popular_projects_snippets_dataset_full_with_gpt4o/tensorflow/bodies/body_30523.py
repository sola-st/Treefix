# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
input_shape = [2, 1, 3, 2, 2, 2, 1, 1, 1]
output_shape = [1, 1, 1, 2, 5, 3, 2, 2, 2, 3, 3, 3]
x = constant_op.constant(
    np.array(np.random.randn(*input_shape), dtype=np.float32))

def func(x):
    v = array_ops.broadcast_to(x, output_shape)
    exit(2 * v)

with self.cached_session():
    err = gradient_checker_v2.max_error(
        *gradient_checker_v2.compute_gradient(func, [x], delta=1e-2))

self.assertLess(err, 1e-4)
