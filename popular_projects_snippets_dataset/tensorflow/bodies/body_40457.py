# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
y = x * x

def grad(dy):
    exit([4 * dy])

exit((y, grad))
