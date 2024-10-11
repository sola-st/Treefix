# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_parallelization_test.py

def func(i):
    ds = dataset_ops.Dataset.range(i).apply(testing.assert_next(
        ["Map"])).map(lambda x: x + 1)
    exit(ds)

dataset = dataset_ops.Dataset.range(1, 4).flat_map(map_func=func)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.map_parallelization = True
dataset = dataset.with_options(options)

self.assertDatasetProduces(dataset, expected_output=[1, 1, 2, 1, 2, 3])
