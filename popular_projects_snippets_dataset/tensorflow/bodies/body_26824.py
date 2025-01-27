# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
dataset = dataset_ops.Dataset.range(5)
if autotune is not False and map_parallelization is not False:  # pylint: disable=g-bool-id-comparison
    dataset = dataset.apply(testing.assert_next(["ParallelMap"]))
else:
    dataset = dataset.apply(testing.assert_next(["Map"]))
dataset = dataset.map(lambda x: x + 1)

options = options_lib.Options()
if autotune is not None:
    options.autotune.enabled = autotune
if map_parallelization is not None:
    options.experimental_optimization.map_parallelization = (
        map_parallelization)
dataset = dataset.with_options(options)

self.assertDatasetProduces(dataset, expected_output=list(range(1, 6)))
