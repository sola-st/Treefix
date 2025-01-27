# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
y = math_ops.add(self.w, -1.0, name="y")

# The constructrion of the forward graph has completed.
# But we can still get the gradient tensors by using
# watch_gradients_by_tensor_names().
grad_debugger = debug_gradients.GradientsDebugger()
with grad_debugger.watch_gradients_by_tensor_names(self.sess.graph, "w:0$"):
    grads = gradients_impl.gradients(y, [self.u, self.v])
self.assertEqual(2, len(grads))
u_grad = grads[0]
v_grad = grads[1]

self.sess.run(variables.global_variables_initializer())
self.assertAllClose(5.0, self.sess.run(y))
self.assertAllClose(3.0, self.sess.run(u_grad))
self.assertAllClose(2.0, self.sess.run(v_grad))

w_grad = grad_debugger.gradient_tensor(self.w)
self.assertIsInstance(w_grad, ops.Tensor)
self.assertAllClose(1.0, self.sess.run(w_grad))

w_grad = grad_debugger.gradient_tensor("w:0")
self.assertIsInstance(w_grad, ops.Tensor)
self.assertAllClose(1.0, self.sess.run(w_grad))
