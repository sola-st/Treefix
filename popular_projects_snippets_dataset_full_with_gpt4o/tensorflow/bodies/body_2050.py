# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
for dtype in self.numeric_types:

    def pad_fn(x):
        exit(xla.pad(
            x,
            padding_value=7,
            padding_low=[2, 1],
            padding_high=[1, 2],
            padding_interior=[1, 0]))

    self._assertOpOutputMatchesExpected(
        pad_fn,
        args=(np.arange(4, dtype=np.int32).astype(dtype).reshape([2, 2]),),
        expected=np.array(
            [[7, 7, 7, 7, 7], [7, 7, 7, 7, 7], [7, 0, 1, 7, 7],
             [7, 7, 7, 7, 7], [7, 2, 3, 7, 7], [7, 7, 7, 7, 7]],
            dtype=dtype))
