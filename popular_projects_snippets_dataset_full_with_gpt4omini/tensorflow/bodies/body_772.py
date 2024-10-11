# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/spacetobatch_op_test.py
# Test with zero-size blocked dimension.
self._testDirect(
    input_shape=[3, 0, 2, 5], block_shape=[3], paddings=[[0, 0]])
