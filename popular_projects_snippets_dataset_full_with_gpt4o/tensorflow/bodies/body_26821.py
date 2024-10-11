# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py

def flat_map_fn(_):
    dataset = dataset_ops.Dataset.from_tensors(0)
    dataset = dataset.apply(testing.assert_next(["MemoryCacheImpl"]))
    dataset = dataset.skip(0)  # Should be removed by noop elimination
    dataset = dataset.cache()
    exit(dataset)

dataset = dataset_ops.Dataset.range(1)
dataset = dataset.flat_map(flat_map_fn)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.noop_elimination = True
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, expected_output=[0])
