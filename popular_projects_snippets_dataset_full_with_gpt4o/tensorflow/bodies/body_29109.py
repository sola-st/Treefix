# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
dataset = dataset_ops.Dataset.range(6)
options = options_lib.Options()
options.experimental_optimization.map_parallelization = (
    map_parallelization)
dataset = dataset.with_options(options)
dataset = self.graphRoundTrip(dataset)
expected = "ParallelMap" if map_parallelization else "Map"
dataset = dataset.apply(testing.assert_next([expected]))
dataset = dataset.map(lambda x: x*x)
self.assertDatasetProduces(dataset, expected_output=[0, 1, 4, 9, 16, 25])
