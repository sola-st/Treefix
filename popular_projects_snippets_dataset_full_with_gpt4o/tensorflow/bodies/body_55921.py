# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
grad = backprop.implicit_grad(loss)()
optimizer.apply_gradients(grad)
