# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
row_lengths = np.random.randint(0, 4, size=128)
values = np.ones(np.sum(row_lengths))
sparse = ragged_tensor.RaggedTensor.from_row_lengths(
    values, row_lengths).to_sparse()
dataset = dataset_ops.Dataset.from_tensor_slices(sparse)
dataset = dataset.batch(32, drop_remainder=True)
dataset = apply_map(dataset, lambda x: x)
self.assertEqual((32, 3), dataset.element_spec.shape)
