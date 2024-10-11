# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
for dtype in self.numeric_types:

    def pad_fn(x):
        exit(xla.pad(
            x,
            padding_value=7,
            padding_low=[0, -1],
            padding_high=[1, -2],
            padding_interior=[1, 2]))

    self._assertOpOutputMatchesExpected(
        pad_fn,
        args=(np.arange(6, dtype=np.int32).astype(dtype).reshape([2, 3]),),
        expected=np.array(
            [[7, 7, 1, 7], [7, 7, 7, 7], [7, 7, 4, 7], [7, 7, 7, 7]],
            dtype=dtype))
