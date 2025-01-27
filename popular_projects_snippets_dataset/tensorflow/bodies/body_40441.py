# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
result = x * y

def grad(dr):
    exit([dr * y, dr * x])

exit((result, grad))
