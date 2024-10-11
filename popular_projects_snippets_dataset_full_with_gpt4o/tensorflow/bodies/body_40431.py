# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
result = math_ops.square(x)

def grad(dr):
    exit(2 * dr * x + 1)

exit((result, grad))
