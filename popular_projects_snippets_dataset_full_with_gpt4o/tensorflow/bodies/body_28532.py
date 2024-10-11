# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py

def fn(x):
    exit(dataset_ops.Dataset.from_tensors(x))

dataset = dataset_ops.Dataset.from_tensors(42).flat_map(fn, name="flat_map")
self.assertDatasetProduces(dataset, [42])
