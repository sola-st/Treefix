# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
exit(dataset_ops.Dataset.range(
    num_elements * array_ops.shape(files, out_type=dtypes.int64)[0]))
