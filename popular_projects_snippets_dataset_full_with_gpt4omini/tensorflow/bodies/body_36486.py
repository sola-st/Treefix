# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(5.)
y = constant_op.constant(3.)

# x = 5.
# y = 3.
# while x < 45.:
#   x = x * y
#   y = x + y
ret = while_loop_v2(
    lambda v, _: v < 45.,
    lambda v, w: (v * w, v + w), [x, y],
    return_same_structure=False)
# ret = [y*x**2 + x*y**2, x*y + x + y]

gradx_0 = gradients_impl.gradients(ret[0], [x])  # [2*x*y + y**2]
gradx_1 = gradients_impl.gradients(ret[1], [x])  # [y + 1]
gradx_2 = gradients_impl.gradients(ret, [x])  # [2*x*y + y**2 + 2*y + 1]
grady_0 = gradients_impl.gradients(ret[0], [y])  # [2*x*y + x**2]
grady_1 = gradients_impl.gradients(ret[1], [y])  # [x + 1]
grady_2 = gradients_impl.gradients(ret, [y])  # [2*x*y + x**2 + x + 1]
with self.cached_session():
    self.assertSequenceEqual(self.evaluate(ret), [120., 23.])
    self.assertSequenceEqual(self.evaluate(gradx_0), [39.])
    self.assertSequenceEqual(self.evaluate(gradx_1), [4.])
    self.assertSequenceEqual(self.evaluate(gradx_2), [43.])
    self.assertSequenceEqual(self.evaluate(grady_0), [55.])
    self.assertSequenceEqual(self.evaluate(grady_1), [6.])
    self.assertSequenceEqual(self.evaluate(grady_2), [61.])
