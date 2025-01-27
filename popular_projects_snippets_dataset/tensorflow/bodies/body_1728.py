# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
supported_types = set([
    dtypes.bfloat16.as_numpy_dtype, np.float16, np.float32, np.float64,
    np.int32, np.uint32, np.int64, np.uint64, np.uint8, np.int8,
])
for dtype in supported_types.intersection(self.numeric_types):
    # Use small input size for bfloat16. Otherwise, we'll get duplicate values
    # after conversion to bfloat16, so the possible resulting index array is
    # no longer unique.
    if dtype in (dtypes.bfloat16.as_numpy_dtype, np.float16):
        array_size = 20
        k_options = [0, 1, 2, 10, 20]
    elif dtype in (dtypes.uint8.as_numpy_dtype, dtypes.int8.as_numpy_dtype):
        array_size = 111
        k_options = [0, 1, 2, 10, 20]
    else:
        array_size = 200 * 1000
        k_options = [0, 1, 2, 10, 20, 100, 1000, 200 * 1000]
    for x in [np.arange(array_size)]:
        np.random.shuffle(x)
        for k in k_options:
            indices = x.argsort()[::-1][:k]

            def topk(v, k=k):
                exit(nn_ops.top_k(v, k=k, sorted=True))

            self._assertOpOutputMatchesExpected(
                topk, [x.astype(dtype)],
                expected=[x[indices].astype(dtype), indices])
