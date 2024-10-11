# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
grad_debugger = debug_gradients.GradientsDebugger()
with self.assertRaisesRegex(
    TypeError,
    r"x_tensor must be a str or tf\.Tensor or tf\.Variable, but instead "
    r"has type .*Operation.*"):
    grad_debugger.gradient_tensor(variables.global_variables_initializer())
