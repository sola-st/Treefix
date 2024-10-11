# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/dense_to_sparse_batch_test.py
exit(dataset_ops.Dataset.from_tensor_slices(components).map(
    lambda x: array_ops.fill([x], x)).apply(
        batching.dense_to_sparse_batch(4, [12])))
