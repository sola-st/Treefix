# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
y = math_ops.add(self.w, -1.0, name="y")
z1 = math_ops.square(y, name="z1")
z2 = math_ops.sqrt(y, name="z2")

grad_debugger_1 = debug_gradients.GradientsDebugger()
with grad_debugger_1.watch_gradients_by_tensors(self.sess.graph, y):
    gradient_descent.GradientDescentOptimizer(0.1).minimize(z1)

grad_debugger_2 = debug_gradients.GradientsDebugger()
with grad_debugger_2.watch_gradients_by_tensors(self.sess.graph, y):
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
