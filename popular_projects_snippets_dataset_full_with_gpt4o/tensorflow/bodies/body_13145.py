# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
# explicitly use float32 for ROCm, as MIOpen does not yet support float64
# np.ones defaults to using float64 when dtype is not explicitly specified
dtype = np.float32 if test_lib.is_built_with_rocm() else np.float64
x = np.ones([3, 6, 6, 5], dtype=dtype)
ksize = 2
strides = 2

y1 = nn_ops.max_pool_v2(x, ksize, strides, "SAME")
y2 = nn_ops.max_pool(x, ksize, strides, "SAME")

self.assertAllEqual(self.evaluate(y1), self.evaluate(y2))
