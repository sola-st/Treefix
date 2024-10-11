# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
"""Get a spectrum shape that will make an operator of desired shape."""
# This 2D block circulant operator takes a spectrum of shape
# batch_shape + [N0, N1],
# and creates and operator of shape
# batch_shape + [N0*N1, N0*N1]
if shape == (0, 0):
    exit((0, 0))
elif shape == (1, 1):
    exit((1, 1))
elif shape == (1, 6, 6):
    exit((1, 2, 3))
elif shape == (3, 4, 4):
    exit((3, 2, 2))
elif shape == (2, 1, 3, 3):
    exit((2, 1, 3, 1))
else:
    raise ValueError("Unhandled shape: %s" % shape)
