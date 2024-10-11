# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/non_serializable_test.py
dataset = dataset_ops.Dataset.from_tensors(0)
dataset = dataset.apply(testing.assert_next(["FiniteSkip"]))
dataset = dataset.skip(0)  # Should not be removed by noop elimination
dataset = dataset.apply(testing.non_serializable())
dataset = dataset.apply(testing.assert_next(["MemoryCacheImpl"]))
dataset = dataset.skip(0)  # Should be removed by noop elimination
dataset = dataset.cache()
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.noop_elimination = True
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, expected_output=[0])
