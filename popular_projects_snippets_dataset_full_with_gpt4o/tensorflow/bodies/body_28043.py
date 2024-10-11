# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
dataset = (
    dataset_ops.Dataset.from_tensor_slices(
        [6, 5, 5, 5, 5]).map(lambda x: array_ops.fill([x], x)).padded_batch(
            batch_size=4, padded_shapes=[5]))
self.assertDatasetProduces(
    dataset, expected_error=(errors.DataLossError, ''))
