# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default(), self.cached_session() as sess:
    v = variables.Variable([1, 2], name="v")
    w = variables.Variable([3, 4], name="w")
    _ = v, w
    uninited = variables.report_uninitialized_variables()
    self.assertAllEqual(np.array([b"v", b"w"]), self.evaluate(uninited))
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(0, self.evaluate(uninited).size)
