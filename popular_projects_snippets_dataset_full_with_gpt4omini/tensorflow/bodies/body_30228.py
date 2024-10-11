# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
cdf = np.array([0, .2, .5, .6, .8, 1.], dtype=np.float32)
arr = np.array([.04, .99, .53, .58, .31, .01, .79, .8, .21],
               dtype=np.float32)
result = np.searchsorted(cdf, arr, side="left")
tf_result = self.evaluate(array_ops.searchsorted(cdf, arr, side="left"))
self.assertAllEqual(result, tf_result)
