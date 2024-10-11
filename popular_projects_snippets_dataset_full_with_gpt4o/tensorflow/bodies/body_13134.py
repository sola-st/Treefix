# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = array_ops.ones([3, 6, 5])
ksize = 2
strides = 2

y1 = nn_ops.avg_pool_v2(x, ksize, strides, "SAME")
y2 = nn_ops.avg_pool1d(x, ksize, strides, "SAME")

self.assertAllEqual(self.evaluate(y1), self.evaluate(y2))
