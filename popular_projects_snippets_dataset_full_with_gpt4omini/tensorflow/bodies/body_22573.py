# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util_test.py
with ops.Graph().as_default() as g:
    self.assertIsNone(training_util.get_global_step())
    self._assert_global_step(training_util.get_or_create_global_step())
    self._assert_global_step(training_util.get_or_create_global_step(g))
