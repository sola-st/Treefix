# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

def Grad(_):
    raise RuntimeError("x")

exit((x, Grad))
