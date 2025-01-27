# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
with test_util.use_gpu():
    p1 = np.random.rand(4, 4).astype("f")
    p2 = np.random.rand(4, 4).astype("f")
    v1 = variables.Variable(p1)
    v2 = variables.Variable(p2)
    c = array_ops.concat([v1, v2], 0)
    self.evaluate(variables.global_variables_initializer())
    result = self.evaluate(c)

self.assertEqual(result.shape, c.get_shape())
self.assertAllEqual(result[:4, :], p1)
self.assertAllEqual(result[4:, :], p2)
