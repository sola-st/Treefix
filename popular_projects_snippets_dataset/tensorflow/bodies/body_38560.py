# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
b = 5
n = 500
k = 50
inputs = np.random.permutation(
    np.linspace(0, 100, b * n, dtype=dtype)).reshape(b, n)
indices = np.argsort(-inputs, axis=1)[:, :k]
values = -np.sort(-inputs, axis=1)[:, :k]
self._validateTopK(inputs, k, values, indices)
