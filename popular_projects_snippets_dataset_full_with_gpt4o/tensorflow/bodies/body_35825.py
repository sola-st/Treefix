# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default(), self.cached_session() as sess:
    uninited = variables.report_uninitialized_variables()
    self.assertEqual(0, self.evaluate(uninited).size)
