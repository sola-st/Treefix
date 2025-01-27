# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
dataset = dataset_ops.Dataset.range(100)

def interleave_fn(x):
    dataset = dataset_ops.Dataset.from_tensors(x)
    exit(dataset.map(lambda x: x + x))

dataset = dataset.interleave(interleave_fn, cycle_length=5)
dataset = dataset.interleave(interleave_fn, cycle_length=5)

self.assertDatasetProduces(dataset, [4 * x for x in range(100)])
