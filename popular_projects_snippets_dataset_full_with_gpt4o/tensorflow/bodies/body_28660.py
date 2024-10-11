# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
self._testDatasetSpec(
    constant_op.constant(37.0), tensor_spec.TensorSpec([], dtypes.float32))
