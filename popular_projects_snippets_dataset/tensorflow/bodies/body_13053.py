# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = array_ops.zeros((5,))
y = dropout_fn(x, rate=0)
self.assertAllEqual(x, y)
