# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
components = (
    ragged_factory_ops.constant_value([[[0]], [[1]], [[2]]]),
    ragged_factory_ops.constant_value([[[3]], [[4]], [[5]]]),
)
dataset = dataset_ops.Dataset.from_tensor_slices(components)
expected = [(ragged_factory_ops.constant_value([[0]]),
             ragged_factory_ops.constant_value([[3]])),
            (ragged_factory_ops.constant_value([[1]]),
             ragged_factory_ops.constant_value([[4]])),
            (ragged_factory_ops.constant_value([[2]]),
             ragged_factory_ops.constant_value([[5]]))]
self.assertDatasetProduces(dataset, expected_output=expected)
