# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(row)
exit(apply_map(dataset, lambda x: control_map_fn(x, num)))
