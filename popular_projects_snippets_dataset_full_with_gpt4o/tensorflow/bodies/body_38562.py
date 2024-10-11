# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
b = 5
n = 500
for k in [1, 5, 50, 500]:
    # Lots of repeated integers taking values in [0, 3]
    inputs = np.random.permutation(
        np.linspace(0, 3, b * n, dtype=np.int32)).reshape(b, n)
    # Use mergesort, a stable sort, to get the indices.
    indices = np.argsort(-inputs, axis=1, kind="mergesort")[:, :k]
    values = -np.sort(-inputs, axis=1)[:, :k]
    self._validateTopK(inputs, k, values, indices)
