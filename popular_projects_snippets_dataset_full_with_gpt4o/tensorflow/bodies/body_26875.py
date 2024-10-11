# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_parallelization_test.py
next_nodes = ["ParallelMap"] if should_optimize else ["Map"]
dataset = dataset_ops.Dataset.range(5).apply(
    testing.assert_next(next_nodes)).map(function)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.map_parallelization = True
dataset = dataset.with_options(options)
self.assertDatasetProduces(
    dataset, expected_output=[function(x) for x in range(5)])
