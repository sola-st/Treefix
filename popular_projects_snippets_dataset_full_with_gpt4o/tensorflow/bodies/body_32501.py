# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
shape = (1000,)
input_op = random_ops.random_normal(shape)
n_ops = self._apply_n_times(array_ops.identity, input_op)
self._run(n_ops, name="NIdentityOps_1000")
