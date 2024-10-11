# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
x = np.arange(1., 25.).reshape([2, 3, 4]).astype(np.float32)
input_tensor = constant_op.constant(x)

def reshape(x):
    exit(array_ops.reshape(x, [1, 8, 3]))

with self.cached_session():
    err = gradient_checker_v2.max_error(
        *gradient_checker_v2.compute_gradient(reshape, [input_tensor]))
    self.assertLess(err, 1e-3)
