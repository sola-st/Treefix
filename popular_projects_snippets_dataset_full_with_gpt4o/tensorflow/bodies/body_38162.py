# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
with test_util.device(use_gpu=use_gpu):
    inx = ops.convert_to_tensor(x)
    ofinite, oinf, onan = math_ops.is_finite(inx), math_ops.is_inf(
        inx), math_ops.is_nan(inx)
    tf_finite, tf_inf, tf_nan = self.evaluate([ofinite, oinf, onan])
if x.dtype == dtypes_lib.bfloat16.as_numpy_dtype:
    # Numpy will implicitly convert bfloat16 value to float16, so we cast to
    # float32 to avoid this.
    x = x.astype(np.float32)
np_finite, np_inf, np_nan = np.isfinite(x), np.isinf(x), np.isnan(x)
self.assertAllEqual(np_inf, tf_inf)
self.assertAllEqual(np_nan, tf_nan)
self.assertAllEqual(np_finite, tf_finite)
self.assertShapeEqual(np_inf, oinf)
self.assertShapeEqual(np_nan, onan)
self.assertShapeEqual(np_finite, ofinite)
