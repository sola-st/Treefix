# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
for dtype in self.float_types:
    self._testTensorArrayGradientWriteReadType(dtype)
for dtype in self.complex_types:
    self._testTensorArrayGradientWriteReadType(dtype)
