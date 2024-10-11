# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(2.)
y = constant_op.constant(3.)
ret = while_loop_v2(
    lambda v: v < 8., lambda v: v * y, [x], return_same_structure=False)
grad = gradients_impl.gradients(ret, [x])
with self.cached_session():
    self.assertEqual(self.evaluate(ret), 18.)
    self.assertSequenceEqual(self.evaluate(grad), [9.])
