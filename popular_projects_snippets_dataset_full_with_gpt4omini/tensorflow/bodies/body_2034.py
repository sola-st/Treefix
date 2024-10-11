# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
if xla_test.test.is_built_with_rocm():
    self.skipTest('Broken with rocm')
for dtype in self.numeric_types:
    self._assertOpOutputMatchesExpected(
        xla.add,
        args=(np.array([1, 2, 3], dtype=dtype),
              np.array([4, 5, 6], dtype=dtype)),
        expected=np.array([5, 7, 9], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        lambda x, y: xla.add(x, y, broadcast_dims=(0,)),
        args=(np.array([[1, 2], [3, 4]], dtype=dtype),
              np.array([7, 11], dtype=dtype)),
        expected=np.array([[8, 9], [14, 15]], dtype=dtype))

    self._assertOpOutputMatchesExpected(
        lambda x, y: xla.add(x, y, broadcast_dims=(1,)),
        args=(np.array([[1, 2], [3, 4]], dtype=dtype),
              np.array([7, 11], dtype=dtype)),
        expected=np.array([[8, 13], [10, 15]], dtype=dtype))
