# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def grad(_):
    raise RuntimeError('x')

exit((x, grad))
