# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sparse_batch_test.py
exit(dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: array_ops.fill([x], x)).sparse_batch(4, [12]))
