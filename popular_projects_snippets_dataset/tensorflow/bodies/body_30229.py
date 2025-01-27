# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
dim_size = 7
for d in range(1, 5):
    shape = [dim_size] * d
    cdf = np.cumsum(
        np.random.uniform(size=shape).astype(np.float32), axis=(d - 1))
    arr = np.random.uniform(size=shape).astype(np.float32) * dim_size

    tf_result = self.evaluate(array_ops.searchsorted(cdf, arr, side="left"))

    cdf = cdf.reshape([-1, dim_size])
    arr = arr.reshape([-1, dim_size])
    result = np.zeros(arr.shape, dtype=np.int32)
    for i in range(dim_size**(d - 1)):
        result[i, :] = np.searchsorted(cdf[i, :], arr[i, :], side="left")

    result = result.reshape(shape)

    self.assertAllEqual(result, tf_result)
