# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
exit(dataset_ops.Dataset.from_tensor_slices(
    sparse_ops.sparse_to_dense(x.indices, x.dense_shape, x.values)))
