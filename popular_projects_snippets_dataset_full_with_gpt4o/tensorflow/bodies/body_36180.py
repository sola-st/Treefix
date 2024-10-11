# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
with self.cached_session():
    x = functional_ops.scan(
        lambda x, _: x, math_ops.range(0), initializer=array_ops.ones([2, 4]))
    self.assertAllEqual([0, 2, 4], x.get_shape())
    self.assertAllEqual(x.get_shape(), self.evaluate(x).shape)
