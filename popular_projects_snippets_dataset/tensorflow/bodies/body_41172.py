# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
exit(backprop.gradients_function(lambda y: y * y, [0])(x)[0])
