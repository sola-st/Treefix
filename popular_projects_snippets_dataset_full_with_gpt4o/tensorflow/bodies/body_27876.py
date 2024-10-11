# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
"""Test a dataset that represents a TensorArray."""
components = (
    tensor_array_ops.TensorArray(dtypes.float32, element_shape=(), size=2)
    .unstack([1.0, 2.0]))

dataset = dataset_ops.Dataset.from_tensors(components)

self.assertDatasetProduces(
    dataset, expected_output=[[1.0, 2.0]], requires_initialization=True)
