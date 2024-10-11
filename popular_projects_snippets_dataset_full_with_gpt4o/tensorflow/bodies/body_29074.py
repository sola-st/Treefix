# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/range_test.py
start, stop = 2, 5
dataset = dataset_ops.Dataset.range(start, stop, output_type=output_type)
expected_output = np.arange(start, stop, dtype=output_type.as_numpy_dtype)
self.assertDatasetProduces(dataset, expected_output=expected_output)
self.assertEqual(output_type, dataset_ops.get_legacy_output_types(dataset))
