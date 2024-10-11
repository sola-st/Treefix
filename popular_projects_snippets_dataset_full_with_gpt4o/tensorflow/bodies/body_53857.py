# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
(a, b) = self.evaluate_if_both_tensors(a, b)
a = self._GetNdArray(a)
b = self._GetNdArray(b)
# When the array rank is small, print its contents. Numpy array printing is
# implemented using inefficient recursion so prints can cause tests to
# time out.
if a.shape != b.shape and (b.ndim <= 3 or b.size < 500):
    shape_mismatch_msg = ("Shape mismatch: expected %s, got %s with contents "
                          "%s.") % (a.shape, b.shape, b)
else:
    shape_mismatch_msg = "Shape mismatch: expected %s, got %s." % (a.shape,
                                                                   b.shape)
self.assertEqual(a.shape, b.shape, shape_mismatch_msg)

msgs = [msg]
# np.allclose does not always work for our custom bfloat16 and float8
# extension types when type promotions are involved, so we first cast any
# arrays of such types to float32.
a_dtype = a.dtype
custom_dtypes = (dtypes.bfloat16.as_numpy_dtype,
                 dtypes.float8_e5m2.as_numpy_dtype,
                 dtypes.float8_e4m3fn.as_numpy_dtype)
a = a.astype(np.float32) if a.dtype in custom_dtypes else a
b = b.astype(np.float32) if b.dtype in custom_dtypes else b
if not np.allclose(a, b, rtol=rtol, atol=atol):
    # Adds more details to np.testing.assert_allclose.
    #
    # NOTE: numpy.allclose (and numpy.testing.assert_allclose)
    # checks whether two arrays are element-wise equal within a
    # tolerance. The relative difference (rtol * abs(b)) and the
    # absolute difference atol are added together to compare against
    # the absolute difference between a and b.  Here, we want to
    # tell user which elements violate such conditions.
    cond = np.logical_or(
        np.abs(a - b) > atol + rtol * np.abs(b),
        np.isnan(a) != np.isnan(b))
    if a.ndim:
        x = a[np.where(cond)]
        y = b[np.where(cond)]
        msgs.append("not close where = {}".format(np.where(cond)))
    else:
        # np.where is broken for scalars
        x, y = a, b
    msgs.append("not close lhs = {}".format(x))
    msgs.append("not close rhs = {}".format(y))
    msgs.append("not close dif = {}".format(np.abs(x - y)))
    msgs.append("not close tol = {}".format(atol + rtol * np.abs(y)))
    msgs.append("dtype = {}, shape = {}".format(a_dtype, a.shape))
    # TODO(xpan): There seems to be a bug:
    # tensorflow/compiler/tests:binary_ops_test pass with float32
    # nan even though the equal_nan is False by default internally.
    np.testing.assert_allclose(
        a, b, rtol=rtol, atol=atol, err_msg="\n".join(msgs), equal_nan=True)
