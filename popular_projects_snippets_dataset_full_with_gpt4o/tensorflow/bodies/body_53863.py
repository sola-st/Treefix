# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Asserts that two numpy arrays or Tensors do not have the same values.

    Args:
      a: the expected numpy ndarray or anything can be converted to one.
      b: the actual numpy ndarray or anything can be converted to one.
      msg: Optional message to report on failure.
    """
try:
    self.assertAllEqual(a, b)
except AssertionError:
    exit()
msg = msg or ""
raise AssertionError("The two values are equal at all elements. %s" % msg)
