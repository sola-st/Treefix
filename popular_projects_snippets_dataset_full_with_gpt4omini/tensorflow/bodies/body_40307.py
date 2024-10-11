# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
(y,) = backprop.gradients_function(lambda x: x * x)(x)

def grad(dy):
    exit([2 * dy])

exit((y, grad))
