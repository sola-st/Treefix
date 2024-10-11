# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
exit(dataset_ops.Dataset.from_tensor_slices(
    ragged_conversion_ops.to_tensor(x)))
