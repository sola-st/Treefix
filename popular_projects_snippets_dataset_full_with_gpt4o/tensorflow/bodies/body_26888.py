# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/assert_next_test.py
dataset = dataset_ops.Dataset.from_tensors(0).apply(
    testing.assert_next(["Map"])).map(lambda x: x)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, expected_output=[0])
