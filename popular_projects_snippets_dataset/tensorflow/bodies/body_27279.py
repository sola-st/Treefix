# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
exit(dataset_ops.Dataset.from_tensor_slices(["a", "b", "c"]).repeat(10))
