# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
mirror_pad_grad = lambda t, paddings: gen_array_ops.mirror_pad_grad(
    t, paddings, "SYMMETRIC")
for dtype in self.numeric_types:
    self._testBinary(
        mirror_pad_grad,
        np.broadcast_to(np.arange(0, 7, dtype=dtype), (3, 2, 1, 7)),
        np.array([
            [1, 1],
            [0, 0],
            [0, 0],
            [2, 2],
        ], dtype=np.int32),
        expected=np.broadcast_to(
            np.array([9, 27, 27], dtype=dtype), (1, 2, 1, 3)))
