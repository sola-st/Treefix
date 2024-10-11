# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
grad_debugger = debug_gradients.GradientsDebugger()
grad_debugger.identify_gradient(self.w)
with self.assertRaisesRegex(ValueError,
                            "The graph already contains an op named .*"):
    grad_debugger.identify_gradient(self.w)
