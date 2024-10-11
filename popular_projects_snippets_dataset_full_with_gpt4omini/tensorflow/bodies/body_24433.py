# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
grad_debugger_1 = debug_gradients.GradientsDebugger()
grad_debugger_2 = debug_gradients.GradientsDebugger()

y = math_ops.add(self.w, -1.0, name="y")
debug_y = grad_debugger_1.identify_gradient(y)
z1 = math_ops.square(debug_y, name="z1")

debug_y = grad_debugger_2.identify_gradient(y)
z2 = math_ops.sqrt(debug_y, name="z2")

with grad_debugger_1:
    gradient_descent.GradientDescentOptimizer(0.1).minimize(z1)
with grad_debugger_2:
    gradient_descent.GradientDescentOptimizer(0.1).minimize(z2)

dz1_dy = grad_debugger_1.gradient_tensor(y)
dz2_dy = grad_debugger_2.gradient_tensor(y)
self.assertIsInstance(dz1_dy, ops.Tensor)
self.assertIsInstance(dz2_dy, ops.Tensor)
self.assertIsNot(dz1_dy, dz2_dy)

self.sess.run(variables.global_variables_initializer())
self.assertAllClose(5.0**2, self.sess.run(z1))
self.assertAllClose(5.0**0.5, self.sess.run(z2))
self.assertAllClose(2.0 * 5.0, self.sess.run(dz1_dy))
self.assertAllClose(0.5 * (5.0**-0.5), self.sess.run(dz2_dy))
