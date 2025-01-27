# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util_test.py
self.assertIsNone(training_util.get_global_step())
with ops.Graph().as_default() as g:
    global_step = training_util.create_global_step()
    self._assert_global_step(global_step)
    self.assertRaisesRegex(ValueError, 'already exists',
                           training_util.create_global_step)
    self.assertRaisesRegex(ValueError, 'already exists',
                           training_util.create_global_step, g)
    self._assert_global_step(training_util.create_global_step(ops.Graph()))
