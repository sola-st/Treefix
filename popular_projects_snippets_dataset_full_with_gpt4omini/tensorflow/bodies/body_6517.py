# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
self.assertTrue(distribute_utils.is_mirrored(var))
self.assertEqual(name, var.name)
self.assertIs(strategy, var.distribute_strategy)
for i, d in enumerate(var._devices):
    self.assertEqual(d, strategy.experimental_local_results(var)[i].device)
    self.assertIs(
        strategy,
        strategy.experimental_local_results(var)[i]._distribute_strategy)  # pylint: disable=protected-access
