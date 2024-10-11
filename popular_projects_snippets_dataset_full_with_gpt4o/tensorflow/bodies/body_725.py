# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/concat_ops_test.py
with self.session():
    p1 = np.random.rand(2, 3).astype("i")
    p2 = np.random.rand(2, 3).astype("i")
    x1 = constant_op.constant(p1)
    x2 = constant_op.constant(p2)
    with self.test_scope():
        c = array_ops.concat([x1, x2], 0)
    result = self.evaluate(c)
self.assertAllEqual(result[:2, :], p1)
self.assertAllEqual(result[2:, :], p2)
