# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
mirror_pad_grad = lambda t, paddings: gen_array_ops.mirror_pad_grad(
    t, paddings, "REFLECT")
for dtype in self.numeric_types:
    self._testBinary(
        mirror_pad_grad,
        np.broadcast_to(
            np.reshape(np.arange(0, 7, dtype=dtype), (7, 1)), (1, 4, 7, 1)),
        np.array([
            [0, 0],
            [1, 1],
            [2, 2],
            [0, 0],
        ], dtype=np.int32),
        expected=np.broadcast_to(
            np.reshape(np.array([16, 18, 8], dtype=dtype), (3, 1)),
            (1, 2, 3, 1)))
