# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
self._testPad(
    inputs=[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
    block_shape=[],
    paddings=[],
    outputs=[[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Same thing, but with a no-op block dim.
self._testPad(
    inputs=[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
    block_shape=[1],
    paddings=[[0, 0]],
    outputs=[[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Same thing, but with two no-op block dims.
self._testPad(
    inputs=[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
    block_shape=[1, 1],
    paddings=[[0, 0], [0, 0]],
    outputs=[[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
