# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.float_types | self.complex_types:
    self._testDivision(dtype)
