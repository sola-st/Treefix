# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util_test.py
with ops.Graph().as_default():
    training_util.create_global_step()
    first = training_util._get_or_create_global_step_read()
    second = training_util._get_or_create_global_step_read()
    self.assertEqual(first, second)
