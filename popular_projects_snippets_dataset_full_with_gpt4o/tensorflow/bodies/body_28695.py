# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_sparse_tensor_slices_test.py
with self.assertRaises(AttributeError):
    dataset_ops.Dataset.from_sparse_tensor_slices(None)
