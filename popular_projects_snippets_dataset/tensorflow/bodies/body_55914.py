# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
grad = backprop.implicit_grad(loss)(self.v)
optimizer.apply_gradients(grad)
exit(self.v.read_value())
