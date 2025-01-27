# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
self._testPad(
    inputs=[[[1, 11], [2, 21], [3, 31]], [[4, 41], [5, 51], [6, 61]]],
    block_shape=[2],
    paddings=[1, 0],
    outputs=[[[0, 0], [2, 21]], [[0, 0], [5, 51]], [[1, 11], [3, 31]],
             [[4, 41], [6, 61]]])
