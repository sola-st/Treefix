# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
self._testDatasetSpec(
    dataset_ops.Dataset.from_tensor_slices(
        constant_op.constant([1, 2, 3])),
    dataset_ops.DatasetSpec(tensor_spec.TensorSpec([], dtypes.int32)))
