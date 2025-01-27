# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
out = x * x

def Grad(*grad):
    exit(3 * grad[0])

exit((out, Grad))
