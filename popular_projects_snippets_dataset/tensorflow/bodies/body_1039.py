# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/einsum_op_test.py
"""Verifies that binary 'op' produces 'expected' when fed 'a' and 'b'."""
with self.session() as session:
    with self.test_scope():
        pa = array_ops.placeholder(dtypes.as_dtype(a.dtype), a.shape, name='a')
        pb = array_ops.placeholder(dtypes.as_dtype(b.dtype), b.shape, name='b')
        output = op(pa, pb)
    result = session.run(output, {pa: a, pb: b})
    self.assertAllCloseAccordingToType(result, expected, rtol=1e-3)
