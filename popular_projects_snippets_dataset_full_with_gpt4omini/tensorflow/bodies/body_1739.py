# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/bucketize_op_test.py
with self.session():
    with self.assertRaisesRegex(TypeError, "Expected list.*"):
        p = array_ops.placeholder(dtypes.int32)
        with self.test_scope():
            math_ops._bucketize(p, boundaries=0)
