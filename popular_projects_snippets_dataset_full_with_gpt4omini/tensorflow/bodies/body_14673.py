# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
b = np_array_ops.array(b, dtype=b_type)
result = test_func(a, b)
if np.issubdtype(result.dtype.as_numpy_dtype, np.inexact):
    self.assertAllClose(result, expected_result)
else:
    self.assertAllEqual(result, expected_result)
