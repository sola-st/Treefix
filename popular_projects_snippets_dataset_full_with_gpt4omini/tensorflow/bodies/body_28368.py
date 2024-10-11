# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
dataset = dataset_ops.Dataset.range(4)
dataset = apply_filter(dataset,
                       lambda x: math_ops.not_equal(math_ops.mod(x, 3), 2))
self.assertDatasetProduces(dataset, expected_output=[0, 1, 3])
