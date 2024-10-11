# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
mask = np.array([]).astype(bool)
arr = np.array([]).astype(np.float32)
numpy_result = arr[mask]
tf_result = array_ops.boolean_mask(arr, mask)
self.assertAllEqual(numpy_result.shape[1:], tf_result.get_shape()[1:])
with self.cached_session():
    self.assertAllClose(numpy_result, tf_result)
