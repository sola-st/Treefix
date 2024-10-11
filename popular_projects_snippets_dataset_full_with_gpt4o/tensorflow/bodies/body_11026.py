# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
out = x

def Grad(_):
    exit((None, None))

exit((out, Grad))
