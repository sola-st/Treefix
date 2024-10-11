# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/spacetobatch_op_test.py
# Test with zero-size remaining dimension.
self._testDirect(
    input_shape=[3, 1, 2, 0], block_shape=[3], paddings=[[0, 2]])
