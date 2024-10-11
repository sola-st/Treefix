# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
def inner():
    exit(v * v)

exit(backprop.implicit_grad(inner)()[0][0])
