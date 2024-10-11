# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = np.ones([3, 7, 6, 6, 5], dtype=np.float32)
ksize = 2
strides = 2

y1 = nn_ops.max_pool_v2(x, ksize, strides, "SAME")
y2 = nn_ops.max_pool3d(x, ksize, strides, "SAME")

self.assertAllEqual(self.evaluate(y1), self.evaluate(y2))
