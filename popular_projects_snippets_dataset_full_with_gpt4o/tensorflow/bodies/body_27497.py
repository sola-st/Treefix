# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/dense_to_sparse_batch_test.py
exit(dataset_ops.Dataset.from_tensors(input_tensor).apply(
    batching.dense_to_sparse_batch(4, [12])))
