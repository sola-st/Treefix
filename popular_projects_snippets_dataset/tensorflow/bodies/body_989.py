# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py

def size_op(x):
    exit(array_ops.size_internal(x, optimize=False, out_type=np.int64))

for dtype in self.numeric_types:
    self._assertOpOutputMatchesExpected(
        size_op,
        np.array([[-1], [1], [4]], dtype=dtype),
        expected=np.int64(3))
