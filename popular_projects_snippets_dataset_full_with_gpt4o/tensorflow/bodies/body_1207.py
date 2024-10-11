# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/complex_div_test.py
with self.session() as session:
    with self.test_scope():
        pa = array_ops.placeholder(dtypes.as_dtype(a.dtype), a.shape, name="a")
        pb = array_ops.placeholder(dtypes.as_dtype(b.dtype), b.shape, name="b")
        output = op(pa, pb)
    result = session.run(output, {pa: a, pb: b})
    if equality_test is None:
        equality_test = self.assertAllCloseAccordingToType
    equality_test(np.real(result), np.real(expected), rtol=1e-3)
    equality_test(np.imag(result), np.imag(expected), rtol=1e-3)
