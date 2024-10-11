# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
accumulator = array_ops.zeros([], dtype=dtypes.int64)
for value in d:
    accumulator += value
exit(accumulator)
