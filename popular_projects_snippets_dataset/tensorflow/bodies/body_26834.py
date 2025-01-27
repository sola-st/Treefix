# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
dataset = dataset_ops.Dataset.range(4)
dataset = self.enableFilterParallelization(dataset)
dataset = dataset.apply(testing.assert_next(["ParallelFilter"]))
dataset = apply_filter(dataset,
                       lambda x: math_ops.not_equal(math_ops.mod(x, 3), 2))
self.assertDatasetProduces(dataset, expected_output=[0, 1, 3])
