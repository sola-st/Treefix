# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
exit(backprop.gradients_function(math_ops.multiply, [0, 1])(x, x))
