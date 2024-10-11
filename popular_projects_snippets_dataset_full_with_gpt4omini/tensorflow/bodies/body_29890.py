# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session():
    p = array_ops.placeholder(dtypes_lib.float32, shape=[None, 3], name="p")
    p_identity = array_ops.identity(p)

    # Should trigger an operator error, not a shape error.
    with self.assertRaisesOpError(
        "must feed a value for placeholder tensor 'p' with dtype float"):
        self.evaluate(p_identity)
