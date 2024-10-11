# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
i = math_ops.argmax(x)
exit(array_ops.stop_gradient(i))
