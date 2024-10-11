# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(5.)
y = constant_op.constant(3.)

# x = 5.
# y = 3.
# while x < 45.:
#   x = x * y
ret = while_loop_v2(
    lambda v, _: v < 45.,
    lambda v, w: (v * w, w), [x, y],
    return_same_structure=False)
# ret = [x*y^2, y]

# Note: This is simply d_ret[0]/d_x since d_ret[1]/d_x is 0.
grad = gradients_impl.gradients(ret, [x])  # [2*x*y]
with self.cached_session():
    self.assertSequenceEqual(self.evaluate(ret), [45., 3.])
    self.assertSequenceEqual(self.evaluate(grad), [9.])
