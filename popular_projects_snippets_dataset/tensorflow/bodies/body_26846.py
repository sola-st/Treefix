# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
dataset = dataset_ops.Dataset.range(4)
options = options_lib.Options()
options.experimental_optimization.filter_parallelization = True
options.autotune.enabled = autotune
dataset = dataset.with_options(options)
if autotune:
    dataset = dataset.apply(testing.assert_next(["ParallelFilter"]))
else:
    dataset = dataset.apply(testing.assert_next(["Filter"]))
dataset = dataset.filter(
    lambda x: math_ops.not_equal(math_ops.mod(x, 3), 2))
self.assertDatasetProduces(dataset, expected_output=[0, 1, 3])
