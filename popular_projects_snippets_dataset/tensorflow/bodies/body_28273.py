# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensors([1.0, 2.0, 3.0])
dataset = apply_map(dataset, dataset_ops.Dataset.from_tensor_slices)
dataset = apply_map(dataset, lambda ds: ds.batch(3)).flat_map(lambda x: x)

self.assertDatasetProduces(dataset, expected_output=[[1.0, 2.0, 3.0]])
