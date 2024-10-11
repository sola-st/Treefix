# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
with test_util.use_gpu():
    p1 = np.random.rand(2, 3).astype("i")
    p2 = np.random.rand(2, 3).astype("i")
    x1 = constant_op.constant(p1)
    x2 = constant_op.constant(p2)
    c = array_ops.concat([x1, x2], 0)
    result = self.evaluate(c)
self.assertAllEqual(result[:2, :], p1)
self.assertAllEqual(result[2:, :], p2)
