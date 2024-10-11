# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
if dtype in self.numeric_types:
    # Use small input size for bfloat16. Otherwise, we'll get duplicate values
    # after conversion to bfloat16, so the possible resulting index array is
    # no longer unique.
    if dtype in (dtypes.bfloat16.as_numpy_dtype, np.float16):
        array_size = 10
        k_options = [0, 1, 2, 10]
    else:
        array_size = 200 * 1000
        k_options = [0, 1, 2, 10, 20, 100, 1000, 200 * 1000]
    batch = 16
    for x in [np.arange(batch * array_size)]:
        np.random.shuffle(x)
        x = np.reshape(x, [batch, array_size])
        for k in k_options:
            indices = x.argsort(axis=1)[::, -1:-k - 1:-1]
            expected = np.sort(x, axis=1)[::, -1:-k - 1:-1]

            def topk(v, k=k):
                exit(nn_ops.top_k(v, k=k, sorted=True))

            self._assertOpOutputMatchesExpected(
                topk, [x.astype(dtype)],
                expected=[expected.astype(dtype), indices])
