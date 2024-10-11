# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
components = (
    ragged_factory_ops.constant_value([[[0]], [[1]], [[2]]]),
    ragged_factory_ops.constant_value([[[3]], [[4]], [[5]]]),
)

dataset = dataset_ops.Dataset.from_tensors(components)

self.assertDatasetProduces(dataset, expected_output=[components])
