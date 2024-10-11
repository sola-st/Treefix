# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
b = 10
n = 5000
inputs = np.random.permutation(
    np.linspace(0, 100, b * n, dtype=dtype)).reshape(b, n)
indices = np.argsort(-inputs, axis=1)
values = -np.sort(-inputs, axis=1)
self._validateTopK(inputs, n, values, indices)
