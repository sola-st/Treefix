# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
# astype and assertAllClose do not properly handle bfloat16 values
np_ans = np_func(x, y)
if np_func != np.true_divide:
    # for true_divide the result is a float, event for integer args.
    np_ans = np_ans.astype(np.float32 if dtype == dtypes_lib.bfloat16
                           else dtype.as_numpy_dtype)
rtol = 1e-2 if dtype in (dtypes_lib.bfloat16, dtypes_lib.float16) else 1e-6
self.assertAllClose(np_ans,
                    self._computeTensorAndLiteral(x, y, dtype, tf_func),
                    rtol=rtol)
self.assertAllClose(np_ans,
                    self._computeLiteralAndTensor(x, y, dtype, tf_func),
                    rtol=rtol)
