# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
for dtype in self.numeric_types:
    self._assertOpOutputMatchesExpected(
        xla.dynamic_slice,
        args=(np.arange(1000,
                        dtype=np.int32).astype(dtype).reshape([10, 10, 10]),
              np.array([5, 7, 3]), np.array([2, 3, 2])),
        expected=np.array(
            np.array([[[573, 574], [583, 584], [593, 594]],
                      [[673, 674], [683, 684], [693, 694]]]),
            dtype=dtype))
