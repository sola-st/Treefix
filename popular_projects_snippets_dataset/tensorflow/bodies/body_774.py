# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/spacetobatch_op_test.py
self._testDirect(
    input_shape=[3, 3, 4, 5, 2],
    block_shape=[3, 4, 2],
    paddings=[[1, 2], [0, 0], [3, 0]])
