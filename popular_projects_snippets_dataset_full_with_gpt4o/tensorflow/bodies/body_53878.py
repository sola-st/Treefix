# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Assert that two given dictionary of tensors are the same.

    Args:
      a: Expected dictionary with numpy ndarray or anything else that can be
        converted to one as values.
      b: Actual dictionary with numpy ndarray or anything else that can be
        converted to one as values.
      msg: Optional message to report on failure.
    """
# To keep backwards compatibility, we first try the base class
# assertDictEqual. If that fails we try the tensorflow one.
try:
    super().assertDictEqual(a, b, msg)
except Exception:  # pylint: disable=broad-except
    self.assertSameElements(a.keys(), b.keys())  # pylint: disable=g-assert-in-except
    for k, v in a.items():
        (a_k, b_k) = self.evaluate_if_both_tensors(v, b[k])
        a_k = self._GetNdArray(a_k)
        b_k = self._GetNdArray(b_k)
        if np.issubdtype(a_k.dtype, np.floating):
            self.assertAllClose(v, b[k], msg=k)
        else:
            self.assertAllEqual(v, b[k], msg=k)
