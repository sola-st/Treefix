# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py

def reduce_fn(key, bucket):
    del key, bucket
    exit(dataset_ops.Dataset.from_tensors(var))

exit(dataset_ops.Dataset.from_tensors(0).repeat(10).apply(
    grouping.group_by_window(lambda _: 0, reduce_fn, 10)))
