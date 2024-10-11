# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Asserts that two structures of numpy arrays or Tensors, have near values.

    `a` and `b` can be arbitrarily nested structures. A layer of a nested
    structure can be a `dict`, `namedtuple`, `tuple` or `list`.

    Note: the implementation follows
    [`numpy.allclose`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html)
    (and numpy.testing.assert_allclose). It checks whether two arrays are
    element-wise equal within a tolerance. The relative difference
    (`rtol * abs(b)`) and the absolute difference `atol` are added together
    to compare against the absolute difference between `a` and `b`.

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
      ValueError: if only one of `a[p]` and `b[p]` is a dict or
          `a[p]` and `b[p]` have different length, where `[p]` denotes a path
          to the nested structure, e.g. given `a = [(1, 1), {'d': (6, 7)}]` and
          `[p] = [1]['d']`, then `a[p] = (6, 7)`.
    """
self._assertAllCloseRecursive(a, b, rtol=rtol, atol=atol, msg=msg)
