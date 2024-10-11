# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/spacetobatch_op_test.py
self._testDirect(
    input_shape=[3, 2, 2, 3, 4, 5, 2, 5],
    block_shape=[1, 1, 3, 4, 2, 2],
    paddings=[[0, 0], [0, 0], [1, 2], [0, 0], [3, 0], [0, 0]])
