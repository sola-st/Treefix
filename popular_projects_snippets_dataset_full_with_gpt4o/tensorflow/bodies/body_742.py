# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/concat_ops_test.py
with self.session():
    with self.test_scope():
        s0 = constant_op.constant(2, dtypes.int32)
        s1 = constant_op.constant(3, dtypes.int32)
        s2 = constant_op.constant(5, dtypes.int32)
        packed = array_ops.stack([s0, s1, s2])
        ans = self.evaluate(packed)
        self.assertAllEqual(ans, [2, 3, 5])
