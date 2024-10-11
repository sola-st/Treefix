# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py

def map_fn(x):
    exit([x])

with self.assertRaisesRegex(
    TypeError, "The `map_func` argument must return a `Dataset` object."):
    dataset_ops.Dataset.from_tensors(42).interleave(
        map_fn, num_parallel_calls=num_parallel_calls)
