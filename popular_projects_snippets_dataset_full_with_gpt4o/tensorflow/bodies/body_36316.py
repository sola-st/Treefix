# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
map_return = map_fn.map_fn(lambda x: 1,
                           constant_op.constant([], dtype=dtypes.int32))
self.assertAllEqual([0], map_return.get_shape().dims)
self.assertAllEqual([0], self.evaluate(map_return).shape)
