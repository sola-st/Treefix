# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
for dtype in self.numeric_types:
    v = np.arange(4, dtype=np.int32).astype(dtype).reshape([2, 2])
    self._assertOpOutputMatchesExpected(
        lambda x: xla.broadcast(x, (7, 42)),
        args=(v,),
        expected=np.tile(v, (7, 42, 1, 1)))
