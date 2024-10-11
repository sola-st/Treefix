# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/memory_cleanup_test.py

def fn(x):
    exit(dataset_ops.Dataset.from_tensors(x * x))

exit(dataset_ops.Dataset.range(0, 100).flat_map(fn))
