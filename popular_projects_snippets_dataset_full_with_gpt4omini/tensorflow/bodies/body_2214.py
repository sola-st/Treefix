# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
shape = list(tensor.shape)
exit(tensor.reshape(
    shape[:ndims - 1] +
    [functools.reduce(lambda x, y: x * y, shape[ndims - 1:], 1)]))
