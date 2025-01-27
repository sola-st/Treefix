# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default(), self.cached_session() as sess:
    v = variables.VariableV1([1, 2], name="v")
    w = variables.VariableV1([3, 4], name="w")
    uninited = variables.report_uninitialized_variables()
    self.assertAllEqual(np.array([b"v", b"w"]), self.evaluate(uninited))
    self.evaluate(w.initializer)
    self.assertAllEqual(np.array([b"v"]), self.evaluate(uninited))
    self.evaluate(v.initializer)
    self.assertEqual(0, self.evaluate(uninited).size)
