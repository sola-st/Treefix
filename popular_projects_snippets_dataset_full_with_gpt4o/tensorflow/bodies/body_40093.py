# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

def grad(unused_dy):
    raise ValueError("test_error_string")

exit((1., grad))
