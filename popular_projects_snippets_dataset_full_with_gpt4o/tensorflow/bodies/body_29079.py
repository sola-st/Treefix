# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/range_test.py
start, stop, step = 10, 2, 2
dataset = dataset_ops.Dataset.range(
    start, stop, step, output_type=output_type)
expected_output = np.arange(
    start, stop, step, dtype=output_type.as_numpy_dtype)
self.assertDatasetProduces(dataset, expected_output=expected_output)
self.assertEqual(output_type, dataset_ops.get_legacy_output_types(dataset))
