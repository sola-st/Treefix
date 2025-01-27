# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
out = (x * x, 2 * y)

def Grad(*grad):
    exit((3 * grad[0], 4 * grad[1]))

exit((out, Grad))
