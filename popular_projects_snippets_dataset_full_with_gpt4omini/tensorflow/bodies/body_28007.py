# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
"""Test a dataset that repeats its input multiple times."""
components = (np.array(1), np.array([1, 2, 3]), np.array(37.0))
dataset = dataset_ops.Dataset.from_tensors(components).repeat(count)
self.assertEqual(
    [c.shape for c in components],
    [shape for shape in dataset_ops.get_legacy_output_shapes(dataset)])
self.assertDatasetProduces(dataset, [components] * count)
