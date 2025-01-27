# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
with self.cached_session():
    map_return = map_fn.map_fn(lambda x: array_ops.zeros([3, 2]),
                               constant_op.constant([]))
    self.assertAllEqual([0, 3, 2], map_return.get_shape().dims)
    self.assertAllEqual([0, 3, 2], self.evaluate(map_return).shape)
