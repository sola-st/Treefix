# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py

def fn(x):
    exit(dataset_ops.Dataset.from_tensors(x))

dataset = dataset_ops.Dataset.from_tensors(42).interleave(
    fn, num_parallel_calls=num_parallel_calls, name="interleave")
self.assertDatasetProduces(dataset, [42])
