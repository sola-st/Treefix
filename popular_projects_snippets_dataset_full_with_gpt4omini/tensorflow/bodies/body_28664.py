# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
self._testDatasetSpec(
    optional_ops.Optional.from_value(37.0),
    optional_ops.OptionalSpec(tensor_spec.TensorSpec([], dtypes.float32)))
