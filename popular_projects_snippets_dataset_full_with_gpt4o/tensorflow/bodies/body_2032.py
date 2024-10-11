# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ensure_shape_op_test.py
with self.session() as sess:
    p = array_ops.placeholder(dtypes.int32)
    with self.test_scope():
        op = check_ops.ensure_shape(p, (None, 3, 3))
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "is not compatible with expected shape"):
        sess.run(op, {p: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]})
