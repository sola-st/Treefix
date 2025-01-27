# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
batch_size = 7
size_search_array = 1000
size_values = 47
cdf = np.cumsum(
    np.random.randint(low=0, high=10,
                      size=[batch_size,
                            size_search_array]).astype(np.int64),
    axis=1)
arr = np.random.randint(
    low=0, high=10 * size_search_array, size=[batch_size,
                                              size_values]).astype(np.int64)

tf_result = self.evaluate(array_ops.searchsorted(cdf, arr, side="left"))

result = np.zeros(arr.shape, dtype=np.int32)
for i in range(batch_size):
    result[i, :] = np.searchsorted(cdf[i, :], arr[i, :], side="left")

self.assertAllEqual(result, tf_result)
