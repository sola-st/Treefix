# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
for dtype in (dtypes.int32, dtypes.int64, dtypes.float32, dtypes.float64,
              dtypes.complex64, dtypes.complex128):
    self._testTensorArrayWriteGradientAddMultipleAdds(dtype)
