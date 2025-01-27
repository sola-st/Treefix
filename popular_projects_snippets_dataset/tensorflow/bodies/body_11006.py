# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
result = x1 * x2

def Grad(dy):
    # Switched the ordering here.
    exit([dy * x1, dy * x2])

exit((result, Grad))
