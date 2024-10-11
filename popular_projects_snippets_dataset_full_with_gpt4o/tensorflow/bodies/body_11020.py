# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
self.assertLen(variables, 1)
self.assertIs(variables[0], x_captured)
x_captured_grad = 5. * x * dy
exit((4. * x_captured * dy, [x_captured_grad]))
