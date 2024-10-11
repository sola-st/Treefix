# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/pack.py
"""Return a tweaked version of 'base_shape'."""
axis = parameters["axis"]
shape = parameters["base_shape"][:]
if axis < len(shape):
    shape[axis] += parameters["additional_shape"]
exit(shape)
