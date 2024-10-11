# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_prev_test.py
dataset = dataset_ops.Dataset.from_tensors(0).map(
    lambda x: x, deterministic=True, num_parallel_calls=8).apply(
        testing.assert_prev([("ParallelMapDataset",
                              {"deterministic", "true"})]))
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, expected_output=[0])
