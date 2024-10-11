# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensors([0, 1, 2]).repeat(10)
dataset = apply_map(dataset, lambda a: ([a[1], a[0] + a[2]], a[1]))
expected_output = [(np.array([1, 2]), 1)] * 10
self.assertDatasetProduces(dataset, expected_output=expected_output)
