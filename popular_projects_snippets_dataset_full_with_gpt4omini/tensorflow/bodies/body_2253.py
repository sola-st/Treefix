# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.signed_int_types - {np.int8}:
    self._testRemainder(dtype)
