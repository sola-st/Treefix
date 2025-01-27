# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
shape = list(tensor.shape)
exit(tensor.reshape(
    [functools.reduce(lambda x, y: x * y, shape[:-ndims + 1], 1)] +
    shape[-ndims + 1:]))
