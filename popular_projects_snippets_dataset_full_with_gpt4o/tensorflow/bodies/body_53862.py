# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Asserts that two numpy arrays or Tensors have the same values.

    Args:
      a: the expected numpy ndarray or anything can be converted to one.
      b: the actual numpy ndarray or anything can be converted to one.
      msg: Optional message to report on failure.
    """
if (ragged_tensor.is_ragged(a) or ragged_tensor.is_ragged(b)):
    exit(self._assertRaggedEqual(a, b, msg))
msg = msg if msg else ""
(a, b) = self.evaluate_if_both_tensors(a, b)
a = self._GetNdArray(a)
b = self._GetNdArray(b)
# Arbitrary bounds so that we don't print giant tensors.
if (b.ndim <= 3 or b.size < 500):
    self.assertEqual(
        a.shape, b.shape, "Shape mismatch: expected %s, got %s."
        " Contents: %r. \n%s." % (a.shape, b.shape, b, msg))
else:
    self.assertEqual(
        a.shape, b.shape, "Shape mismatch: expected %s, got %s."
        " %s" % (a.shape, b.shape, msg))

same = (a == b)

if dtypes.as_dtype(a.dtype).is_floating:
    same = np.logical_or(same, np.logical_and(np.isnan(a), np.isnan(b)))
msgs = [msg]
if not np.all(same):
    # Adds more details to np.testing.assert_array_equal.
    diff = np.logical_not(same)
    if a.ndim:
        x = a[np.where(diff)]
        y = b[np.where(diff)]
        msgs.append("not equal where = {}".format(np.where(diff)))
    else:
        # np.where is broken for scalars
        x, y = a, b
    msgs.append("not equal lhs = %r" % x)
    msgs.append("not equal rhs = %r" % y)

    if (a.dtype.kind != b.dtype.kind and
        {a.dtype.kind, b.dtype.kind}.issubset({"U", "S", "O"})):
        a_list = []
        b_list = []
        # OK to flatten `a` and `b` because they are guaranteed to have the
        # same shape.
        for out_list, flat_arr in [(a_list, a.flat), (b_list, b.flat)]:
            for item in flat_arr:
                if isinstance(item, str):
                    out_list.append(item.encode("utf-8"))
                else:
                    out_list.append(item)
        a = np.array(a_list)
        b = np.array(b_list)

    np.testing.assert_array_equal(a, b, err_msg="\n".join(msgs))
