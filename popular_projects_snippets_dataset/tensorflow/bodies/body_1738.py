# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/bucketize_op_test.py
with self.session() as sess:
    p = array_ops.placeholder(dtypes.int32)
    with self.test_scope():
        op = math_ops._bucketize(p, boundaries=[0, 8, 3, 11])
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "Expected sorted boundaries"):
        sess.run(op, {p: [-5, 0]})
