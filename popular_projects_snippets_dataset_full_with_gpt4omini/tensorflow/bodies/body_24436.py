# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
grad_debugger = debug_gradients.GradientsDebugger()
id_grad_w = grad_debugger.identify_gradient(self.w)
y = math_ops.add(id_grad_w, -1.0, name="y")

with grad_debugger:
    gradient_descent.GradientDescentOptimizer(0.1).minimize(y)

self.sess.run(variables.global_variables_initializer())

# Fetch the gradient tensor with the x-tensor object.
w_grad = grad_debugger.gradient_tensor(self.w)
self.assertIsInstance(w_grad, ops.Tensor)
self.assertAllClose(1.0, self.sess.run(w_grad))
