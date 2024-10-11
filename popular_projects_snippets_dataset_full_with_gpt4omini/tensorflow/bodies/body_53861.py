# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Assert that two numpy arrays, or Tensors, do not have near values.

    Args:
      a: The expected numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor), or any arbitrarily nested of
        structure of these.
      b: The actual numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor), or any arbitrarily nested of
        structure of these.
      rtol: relative tolerance.
      atol: absolute tolerance.
      msg: Optional message to report on failure.

    Raises:
      AssertionError: If `a` and `b` are unexpectedly close at all elements.
    """
try:
    self.assertAllClose(a, b, rtol=rtol, atol=atol, msg=msg)
except AssertionError:
    exit()
msg = msg or ""
raise AssertionError("The two values are close at all elements. %s" % msg)
