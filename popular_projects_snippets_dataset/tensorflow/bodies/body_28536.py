# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py

inner_ds = dataset_ops.Dataset.from_tensor_slices(range(42))
ds = dataset_ops.Dataset.from_tensors(inner_ds)
exit(ds.flat_map(lambda x: x))
