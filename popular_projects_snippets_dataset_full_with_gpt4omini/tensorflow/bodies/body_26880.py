# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_parallelization_test.py
next_nodes = ["ParallelMap"] if (apply_autotune is not False) else ["Map"]  # pylint: disable=g-bool-id-comparison
dataset = dataset_ops.Dataset.range(4).apply(
    testing.assert_next(next_nodes)).map(lambda x: x + 2)

options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.map_parallelization = True
if apply_autotune is not None:
    options.autotune.enabled = apply_autotune
dataset = dataset.with_options(options)
self.assertDatasetProduces(dataset, expected_output=[2, 3, 4, 5])
