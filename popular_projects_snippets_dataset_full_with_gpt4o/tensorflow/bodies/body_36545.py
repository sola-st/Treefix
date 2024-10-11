# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
param = constant_op.constant(2.0)
y0 = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name="elems")
# map_fn uses TensorArray internally.
r = map_fn.map_fn(lambda x: math_ops.multiply(x, param), y0)
grad = gradients_impl.gradients(r, param)[0]
self.assertAllClose([2.0, 4.0, 6.0, 8.0, 10.0, 12.0], self.evaluate(r))
self.assertAllClose(21.0, self.evaluate(grad))
