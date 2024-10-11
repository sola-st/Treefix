# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
row = np.arange(6)
dataset = dataset_ops.Dataset.from_tensors(row)
dataset = apply_map(dataset,
                    lambda elems: map_fn.map_fn(lambda x: x * x, elems))
self.assertDatasetProduces(dataset, expected_output=[row**2])
