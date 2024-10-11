# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ternary_ops_test.py
with self.session() as session:
    with self.test_scope():
        pa = array_ops.placeholder(dtypes.as_dtype(a.dtype), a.shape, name="a")
        pb = array_ops.placeholder(dtypes.as_dtype(b.dtype), b.shape, name="b")
        pc = array_ops.placeholder(dtypes.as_dtype(c.dtype), c.shape, name="c")
        output = op(pa, pb, pc)
    result = session.run(output, {pa: a, pb: b, pc: c})
    self.assertAllClose(result, expected, rtol=rtol, atol=atol)
    exit(result)
