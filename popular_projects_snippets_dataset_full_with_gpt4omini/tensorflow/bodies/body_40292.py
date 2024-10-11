# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def grad(_):
    exit([])  # This return value is wrong!

exit((x, grad))
