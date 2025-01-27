# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
t = array_ops.ones([2, 4, 3])
v = array_ops.ones([2, 5, 3])
strides = 2

y1 = nn_ops.conv1d_transpose(t, v, [2, 8, 5], strides)
y2 = nn_ops.conv_transpose(t, v, [2, 8, 5], strides)

self.assertAllEqual(self.evaluate(y1), self.evaluate(y2))
