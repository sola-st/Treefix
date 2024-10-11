# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
self._testPad(
    inputs=[[1, 2, 3], [4, 5, 6]],
    block_shape=[2],
    paddings=[1, 0],
    outputs=[[0, 2], [0, 5], [1, 3], [4, 6]])
