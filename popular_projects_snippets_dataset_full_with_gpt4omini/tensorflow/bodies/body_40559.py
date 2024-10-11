# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
flatten_layer = core.Flatten()
x = constant_op.constant([[[-10, -20], [-30, -40]], [[10, 20], [30, 40]]])
y = flatten_layer(x)
self.assertAllEqual([[-10, -20, -30, -40], [10, 20, 30, 40]], y)
