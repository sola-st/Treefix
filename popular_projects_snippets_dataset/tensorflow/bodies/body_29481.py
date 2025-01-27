# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
input_ = (
    input_ if input_ is not None else array_ops.zeros(
        shape, dtype=updates.dtype))
exit(array_ops.scatter_nd_non_aliasing_add(input_, indices, updates))
