# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
x = array_ops.placeholder(dtypes.float32)
y = map_fn.map_fn(lambda e: e, x)
self.assertIs(None, y.get_shape().dims)
