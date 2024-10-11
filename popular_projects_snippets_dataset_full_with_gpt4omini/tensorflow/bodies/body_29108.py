# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
dataset = dataset_ops.Dataset.range(5)
options = options_lib.Options()
options.experimental_slack = True
options.experimental_optimization.apply_default_optimizations = False
dataset = dataset.with_options(options)
dataset = self.graphRoundTrip(dataset)
result = self._get_options(dataset)
self.assertTrue(result.experimental_slack)
# Explicitly check that flag is False since assertFalse allows None
self.assertIs(
    result.experimental_optimization.apply_default_optimizations, False)
