# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/concat.py
"""Return a tweaked version of 'base_shape'."""
axis = parameters["axis"]
shape = parameters["base_shape"][:]
if axis < 0:
    axis += len(shape)
if axis < len(shape):
    shape[axis] += delta
exit(shape)
