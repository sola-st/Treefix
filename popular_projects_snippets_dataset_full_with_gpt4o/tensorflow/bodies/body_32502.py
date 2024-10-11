# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
shape = (1000,)
input_op = random_ops.random_normal(shape)
n_ensure_ops = self._apply_n_times(
    lambda x: check_ops.ensure_shape(array_ops.identity(x), shape),
    input_op)
self._run(n_ensure_ops, name="NEnsureShapeAndIdentityOps_1000")
