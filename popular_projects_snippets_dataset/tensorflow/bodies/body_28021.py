# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
components = ()

with self.assertRaises(ValueError):
    dataset_ops.Dataset.from_tensor_slices(components)
