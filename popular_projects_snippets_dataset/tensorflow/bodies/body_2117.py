# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/manip_ops_test.py
with self.session() as session:
    with self.test_scope():
        p = array_ops.placeholder(dtypes.as_dtype(a.dtype), a.shape, name="a")
        output = manip_ops.roll(a, shift, axis)
    result = session.run(output, {p: a})
    self.assertAllEqual(result, np.roll(a, shift, axis))
