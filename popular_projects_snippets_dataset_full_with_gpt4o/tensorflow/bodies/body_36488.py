# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(2.)
ret1 = while_loop_v2(
    lambda v: v < 4., lambda v: v * v, [x],
    return_same_structure=False)  # x**2
ret2 = while_loop_v2(
    lambda v: v < 16., lambda v: v * v, [ret1],
    return_same_structure=False)  # x**4
grad = gradients_impl.gradients(ret2, [x])  # 4x**3
grad_grad = gradients_impl.gradients(grad, [x])  # 12x**2
with self.cached_session():
    self.assertSequenceEqual(self.evaluate(grad), [32.])
    self.assertSequenceEqual(self.evaluate(grad_grad), [48.])
