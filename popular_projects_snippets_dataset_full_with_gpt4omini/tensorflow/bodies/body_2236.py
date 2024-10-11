# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
with self.session() as session:
    with self.test_scope():
        pa = array_ops.placeholder(dtypes.as_dtype(a.dtype), a.shape, name="a")
        pb = array_ops.placeholder(dtypes.as_dtype(b.dtype), b.shape, name="b")
        output = op(pa, pb)
    result = session.run(output, {pa: a, pb: b})
    if equality_test is None:
        equality_test = self.assertAllCloseAccordingToType
    if rtol is None:
        rtol = 1e-15 if a.dtype == np.float64 else 1e-3
    if atol is None:
        atol = 1e-15 if a.dtype == np.float64 else 1e-6
    equality_test(result, expected, rtol=rtol, atol=atol)
