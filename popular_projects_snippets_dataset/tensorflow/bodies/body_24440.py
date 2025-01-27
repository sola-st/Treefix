# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
y = math_ops.add(self.w, -1.0, name="y")

grad_debugger = debug_gradients.GradientsDebugger()
with grad_debugger.watch_gradients_by_tensor_names(self.sess.graph,
                                                   "(u|w):0$"):
    grads = gradients_impl.gradients(y, [self.u, self.v])
self.assertEqual(2, len(grads))
u_grad = grads[0]

self.assertEqual(2, len(grad_debugger.gradient_tensors()))
self.assertIs(u_grad, grad_debugger.gradient_tensor("u:0"))
self.assertIsInstance(grad_debugger.gradient_tensor("w:0"), ops.Tensor)

self.sess.run(variables.global_variables_initializer())
self.assertAllClose(1.0, self.sess.run(
    grad_debugger.gradient_tensor("w:0")))
self.assertAllClose(3.0, self.sess.run(
    grad_debugger.gradient_tensor("u:0")))
