# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def grad(dresult):
    exit([2 * dresult])

exit((x, grad))
