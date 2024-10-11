# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/skip_test.py
components = (np.arange(10),)
dataset = dataset_ops.Dataset.from_tensor_slices(components).skip(count)
self.assertEqual(
    [c.shape[1:] for c in components],
    [shape for shape in dataset_ops.get_legacy_output_shapes(dataset)])
start_range = min(count, 10) if count != -1 else 10
self.assertDatasetProduces(
    dataset,
    [tuple(components[0][i:i + 1]) for i in range(start_range, 10)])
