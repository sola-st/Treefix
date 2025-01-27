# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util_test.py
with ops.Graph().as_default():
    self.assertIsNone(training_util._get_or_create_global_step_read())
    training_util.create_global_step()
    self.assertIsNotNone(training_util._get_or_create_global_step_read())
