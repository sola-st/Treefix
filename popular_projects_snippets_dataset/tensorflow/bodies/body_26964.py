# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
elements = list(range(1000))
dataset = dataset_ops.Dataset.from_tensor_slices(elements)
self.assertDatasetProduces(dataset, expected_output=elements)
