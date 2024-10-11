# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
z = f(y)
exit(array_ops.stop_gradient(z))
