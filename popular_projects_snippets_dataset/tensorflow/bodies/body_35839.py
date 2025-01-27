# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
for dtype in [
    np.float16, np.float32, np.float64, np.complex64, np.complex128,
    np.int32, np.int64, dtypes.bfloat16.as_numpy_dtype
]:
    self.setUp()
    x = vals.astype(dtype)
    tftype = _NP_TO_TF[dtype]
    self.assertAllEqual(x, self._initFetch(x, tftype, use_gpu=False))
    # NOTE(touts): the GPU test should pass for all types, whether the
    # Variable op has an implementation for that type on GPU as we expect
    # that Variable and Assign have GPU implementations for matching tf.
    self.assertAllEqual(x, self._initFetch(x, tftype, use_gpu=True))
