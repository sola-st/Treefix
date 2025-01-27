# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

def Grad(dy):
    exit([3 * dy])

exit((x, Grad))
