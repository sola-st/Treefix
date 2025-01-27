# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
with self.cached_session():
    param = constant_op.constant(2.0)
    elems = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name="elems")
    y = map_fn.map_fn(
        lambda x: math_ops.multiply(math_ops.square(x), param), elems)
    r_param = gradients_impl.gradients(y, param)[0]
    r_elems = gradients_impl.gradients(y, elems)[0]
    self.assertAllEqual(91.0, self.evaluate(r_param))
    self.assertAllEqual([4.0, 8.0, 12.0, 16.0, 20.0, 24.0],
                        self.evaluate(r_elems))
