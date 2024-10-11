# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for rank in range(1, _MAX_RANK + 1):
    np_arr = self._makeIncremental((2,) * rank, dtypes.bfloat16) * \
               np.array([0.01]).astype(dtypes.bfloat16.as_numpy_dtype)
    self._compareAllAxes(np_arr, rtol=1e-2, atol=1e-2)
