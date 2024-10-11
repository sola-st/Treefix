# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Like assertAllClose, but also suitable for comparing fp16 arrays.

    In particular, the tolerance is reduced to 1e-3 if at least
    one of the arguments is of type float16.

    Args:
      a: the expected numpy ndarray or anything can be converted to one.
      b: the actual numpy ndarray or anything can be converted to one.
      rtol: relative tolerance.
      atol: absolute tolerance.
      float_rtol: relative tolerance for float32.
      float_atol: absolute tolerance for float32.
      half_rtol: relative tolerance for float16.
      half_atol: absolute tolerance for float16.
      bfloat16_rtol: relative tolerance for bfloat16.
      bfloat16_atol: absolute tolerance for bfloat16.
      msg: Optional message to report on failure.
    """
(a, b) = self.evaluate_if_both_tensors(a, b)
a = self._GetNdArray(a)
b = self._GetNdArray(b)
# types with lower tol are put later to overwrite previous ones.
if (a.dtype == np.float32 or b.dtype == np.float32 or
    a.dtype == np.complex64 or b.dtype == np.complex64):
    rtol = max(rtol, float_rtol)
    atol = max(atol, float_atol)
if a.dtype == np.float16 or b.dtype == np.float16:
    rtol = max(rtol, half_rtol)
    atol = max(atol, half_atol)
if (a.dtype == dtypes.bfloat16.as_numpy_dtype or
    b.dtype == dtypes.bfloat16.as_numpy_dtype):
    rtol = max(rtol, bfloat16_rtol)
    atol = max(atol, bfloat16_atol)

self.assertAllClose(a, b, rtol=rtol, atol=atol, msg=msg)
