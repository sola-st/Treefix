# Extracted from ./data/repos/tensorflow/tensorflow/core/config/flags_test.py
self.assertTrue(flags.config().test_only_experiment_1.value())
self.assertFalse(flags.config().test_only_experiment_2.value())

flags.config().test_only_experiment_1.reset(False)
flags.config().test_only_experiment_2.reset(True)

self.assertFalse(flags.config().test_only_experiment_1.value())
self.assertTrue(flags.config().test_only_experiment_2.value())
