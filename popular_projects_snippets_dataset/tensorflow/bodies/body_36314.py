# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
x = constant_op.constant([[1, 2, 3], [4, 5, 6]])
y = map_fn.map_fn(lambda e: e, x)
self.assertAllEqual(y.get_shape(), self.evaluate(y).shape)
