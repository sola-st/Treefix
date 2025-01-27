# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/dense_update_ops_test.py
for dtype in [
    np.float32, np.float64, np.int32, np.int64,
    dtypes.bfloat16.as_numpy_dtype
]:
    x = np.zeros(vals.shape).astype(dtype)
    y = vals.astype(dtype)
    var_value, op_value = self._initAssignFetch(x, y, use_gpu=False)
    self.assertAllEqual(y, var_value)
    self.assertAllEqual(y, op_value)
    var_value, op_value = self._initAssignAddFetch(x, y, use_gpu=False)
    self.assertAllEqual(x + y, var_value)
    self.assertAllEqual(x + y, op_value)
    var_value, op_value = self._initAssignSubFetch(x, y, use_gpu=False)
    self.assertAllEqual(x - y, var_value)
    self.assertAllEqual(x - y, op_value)
    if test.is_built_with_gpu_support() and dtype in [np.float32, np.float64]:
        var_value, op_value = self._initAssignFetch(x, y, use_gpu=True)
        self.assertAllEqual(y, var_value)
        self.assertAllEqual(y, op_value)
        var_value, op_value = self._initAssignAddFetch(x, y, use_gpu=True)
        self.assertAllEqual(x + y, var_value)
        self.assertAllEqual(x + y, op_value)
        var_value, op_value = self._initAssignSubFetch(x, y, use_gpu=True)
        self.assertAllEqual(x - y, var_value)
        self.assertAllEqual(x - y, op_value)
