# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
y = math_ops.add(self.w, -1.0, name="foo/y")
z = math_ops.square(y, name="foo/z")

# The constructrion of the forward graph has completed.
# But we can still get the gradient tensors by using
# watch_gradients_by_x_tensors().
grad_debugger = debug_gradients.GradientsDebugger()
with grad_debugger.watch_gradients_by_tensors(self.sess.graph,
                                              [self.w, self.u, y]):
    gradient_descent.GradientDescentOptimizer(0.1).minimize(z)

self.assertEqual(3, len(grad_debugger.gradient_tensors()))
u_grad = grad_debugger.gradient_tensor(self.u)
w_grad = grad_debugger.gradient_tensor(self.w)
y_grad = grad_debugger.gradient_tensor(y)

self.sess.run(variables.global_variables_initializer())
self.assertAllClose(10.0, self.sess.run(y_grad))
self.assertAllClose(10.0, self.sess.run(w_grad))
self.assertAllClose(30.0, self.sess.run(u_grad))
