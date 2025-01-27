# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default(), self.cached_session() as sess:
    v = variables.Variable(array_ops.zeros([0, 2]), name="v")
    uninited = variables.report_uninitialized_variables()
    self.evaluate(v.initializer)  # not strictly necessary
    self.assertEqual(0, self.evaluate(uninited).size)
