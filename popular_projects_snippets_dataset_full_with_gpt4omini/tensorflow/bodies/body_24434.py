# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
grad_debugger_1 = debug_gradients.GradientsDebugger()
grad_debugger_2 = debug_gradients.GradientsDebugger()
id_grad_w = grad_debugger_1.identify_gradient(self.w)
y = math_ops.add(id_grad_w, -1.0, name="y")

# There are >1 gradient debuggers registered, and grad_debugger is not used
# as a context manager here, so the gradient w.r.t. self.w will not be
# registered.
gradients_impl.gradients(y, [self.u, self.v])

with self.assertRaisesRegex(
    LookupError,
    r"This GradientsDebugger has not received any gradient tensor for "):
    grad_debugger_1.gradient_tensor(self.w)
with self.assertRaisesRegex(
    LookupError,
    r"This GradientsDebugger has not received any gradient tensor for "):
    grad_debugger_2.gradient_tensor(self.w)
