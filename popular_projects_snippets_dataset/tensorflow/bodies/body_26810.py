# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py

def map_fn(x):
    exit(x + var)

exit(dataset_ops.Dataset.from_tensors(0).apply(
    batching.map_and_batch(map_fn, 1)))
