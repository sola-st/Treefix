# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
for dtype in (np.float32, np.float64, np.complex64, np.complex128):
    self._testTensorArrayGradientWriteReadType(dtype)
