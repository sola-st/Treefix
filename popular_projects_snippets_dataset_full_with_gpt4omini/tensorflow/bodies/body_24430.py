# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
grad_debugger = debug_gradients.GradientsDebugger()
id_grad_w = grad_debugger.identify_gradient(self.w)
y = math_ops.add(id_grad_w, -1.0, name="y")

grads = gradients_impl.gradients(y, [self.u, self.v])
self.assertEqual(2, len(grads))
u_grad = grads[0]
v_grad = grads[1]

self.sess.run(variables.global_variables_initializer())
self.assertAllClose(5.0, self.sess.run(y))
self.assertAllClose(3.0, self.sess.run(u_grad))
self.assertAllClose(2.0, self.sess.run(v_grad))

# Fetch the gradient tensor with the x-tensor object.
w_grad = grad_debugger.gradient_tensor(self.w)
self.assertIsInstance(w_grad, ops.Tensor)
self.assertAllClose(1.0, self.sess.run(w_grad))

# Fetch the gradient tensor with the x-tensor's name.
w_grad = grad_debugger.gradient_tensor(self.w.name)
self.assertIsInstance(w_grad, ops.Tensor)
self.assertAllClose(1.0, self.sess.run(w_grad))

# Fetch the gradient tensor with the x-tensor name.
w_grad = grad_debugger.gradient_tensor(self.w.name)
self.assertIsInstance(w_grad, ops.Tensor)
self.assertAllClose(1.0, self.sess.run(w_grad))
