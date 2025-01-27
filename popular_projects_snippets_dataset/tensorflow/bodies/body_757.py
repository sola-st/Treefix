# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/spacetobatch_op_test.py
x_np = [[[[1], [2]], [[3], [4]]]]
paddings = np.array([[1, 0], [1, 0]], dtype=np.int32)
block_size = 3
x_out = [[[[0]]], [[[0]]], [[[0]]], [[[0]]], [[[1]]], [[[2]]], [[[0]]],
         [[[3]]], [[[4]]]]
self._testPad(x_np, paddings, block_size, x_out)
