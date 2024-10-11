# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unpack.py
"""Return a tweaked version of 'axis'."""
axis = parameters["axis"]
shape = parameters["base_shape"][:]
while axis > len(shape) - 1:
    axis -= 1
exit(axis)
