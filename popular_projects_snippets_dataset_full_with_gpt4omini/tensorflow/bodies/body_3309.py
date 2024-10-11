# Extracted from ./data/repos/tensorflow/tensorflow/core/config/flags_test.py
flags.config().test_only_experiment_1.reset(False)
self.assertFalse(flags.config().test_only_experiment_1.value())

# Get second reference to underlying Flags singleton.
flag = flags.flags_pybind.Flags()
flag.test_only_experiment_1.reset(True)

# check that both references are correctly updated.
self.assertTrue(flags.config().test_only_experiment_1.value())
self.assertTrue(flag.test_only_experiment_1.value())
