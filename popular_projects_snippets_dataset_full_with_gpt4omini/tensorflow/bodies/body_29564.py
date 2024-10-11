# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
# Test with zero-size remaining dimension.
self._testDirect(
    input_shape=[3, 1, 2, 0], block_shape=[3], paddings=[[0, 2]])

# Test with zero-size blocked dimension.
self._testDirect(
    input_shape=[3, 0, 2, 5], block_shape=[3], paddings=[[0, 0]])

# Test with padding up from zero size.
self._testDirect(
    input_shape=[3, 0, 2, 5], block_shape=[3], paddings=[[1, 2]])

self._testDirect(
    input_shape=[3, 3, 4, 5, 2],
    block_shape=[3, 4, 2],
    paddings=[[1, 2], [0, 0], [3, 0]])

self._testDirect(
    input_shape=[3, 3, 4, 5, 2],
    block_shape=[3, 4, 2, 2],
    paddings=[[1, 2], [0, 0], [3, 0], [0, 0]])

self._testDirect(
    input_shape=[3, 2, 2, 3, 4, 5, 2, 5],
    block_shape=[1, 1, 3, 4, 2, 2],
    paddings=[[0, 0], [0, 0], [1, 2], [0, 0], [3, 0], [0, 0]])

self._testDirect(
    input_shape=[3, 2, 2, 3, 4, 5, 2, 5],
    block_shape=[1, 1, 3, 4, 2, 2, 1],
    paddings=[[0, 0], [0, 0], [1, 2], [0, 0], [3, 0], [0, 0], [0, 0]])
