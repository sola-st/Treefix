# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py

def map_fn(i):
    exit(dataset_ops.Dataset.from_tensors(i))

dataset = dataset_ops.Dataset.range(10).map(map_fn).batch(5)
dataset = dataset.map(lambda x: x)
dataset = dataset.unbatch().flat_map(lambda x: x)
self.assertDatasetProduces(dataset, expected_output=range(10))
