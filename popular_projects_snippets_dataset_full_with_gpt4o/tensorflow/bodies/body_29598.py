# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
self._test(
    input_shape=np.zeros((0,), np.int32),
    block_shape=np.zeros((0,), np.int32),
    base_paddings=None)
self._test(
    input_shape=np.zeros((0,), np.int32),
    block_shape=np.zeros((0,), np.int32),
    base_paddings=np.zeros((0, 2), np.int32))
self._test(input_shape=[1], block_shape=[2], base_paddings=None)
self._test(input_shape=[1], block_shape=[2], base_paddings=[[1, 0]])
self._test(input_shape=[3], block_shape=[1], base_paddings=[[1, 2]])
self._test(input_shape=[1], block_shape=[2], base_paddings=[[2, 3]])
self._test(input_shape=[4, 5], block_shape=[3, 2], base_paddings=None)
self._test(
    input_shape=[4, 5], block_shape=[3, 2], base_paddings=[[0, 0], [0, 1]])
