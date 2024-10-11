# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
value = backprop.gradients_function(sq, [0])(x)[0]
exit(value)
