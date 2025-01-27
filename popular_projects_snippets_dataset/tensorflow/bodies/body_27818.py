# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sparse_batch_test.py
exit(dataset_ops.Dataset.from_tensors(input_tensor).sparse_batch(
    4, [12]))
