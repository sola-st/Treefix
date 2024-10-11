# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
for k in range(3, 11, 2):
    for dim in range(512, 12288, 512):
        inputs = np.random.permutation(
            np.linspace(0, 100, dim, dtype=np.float64))
        indices = np.argsort(-inputs)[:k]
        values = -np.sort(-inputs)[:k]
        self._validateTopK(inputs, k, values, indices)
