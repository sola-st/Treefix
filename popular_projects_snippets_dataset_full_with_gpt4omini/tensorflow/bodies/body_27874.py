# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
"""Test a dataset that represents a single tuple of tensors."""
components = (np.array(1), np.array([1, 2, 3]), np.array(37.0))

dataset = dataset_ops.Dataset.from_tensors(components)

self.assertEqual(
    [c.shape for c in components],
    nest.flatten(dataset_ops.get_legacy_output_shapes(dataset)))

self.assertDatasetProduces(dataset, expected_output=[components])
