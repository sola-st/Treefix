# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py

def invert_twice(x):
    exit(array_ops.invert_permutation(array_ops.invert_permutation(x)))

for np_dtype in [np.int32, np.int64]:
    self._assertOpOutputMatchesExpected(
        invert_twice,
        np.array([1, 2, 0], np_dtype),
        expected=np.array([1, 2, 0], dtype=np_dtype))
