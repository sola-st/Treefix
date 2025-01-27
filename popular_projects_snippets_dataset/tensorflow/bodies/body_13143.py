# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
dtype = np.float32 if test_lib.is_built_with_rocm() else np.float64
x = np.array([[[3], [6], [5]], [[1], [0], [1]]], dtype=dtype)
ksize = 2
strides = 1
y = nn_ops.max_pool1d(x, ksize, strides, "SAME")
expected_y = np.array([[[6], [6], [5]], [[1], [1], [1]]], dtype=dtype)
self.assertAllEqual(self.evaluate(y), expected_y)
