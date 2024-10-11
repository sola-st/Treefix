# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
out = x

def Grad(*grad):
    exit(grad)

exit((out, Grad))
