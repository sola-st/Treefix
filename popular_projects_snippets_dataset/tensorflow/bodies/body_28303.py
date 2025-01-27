# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensors((42, None))

def map_function(x, y):
    if y is None:
        exit(x / 2)
    exit(x)

dataset = apply_map(dataset, map_function)
self.assertDatasetProduces(dataset, expected_output=[21])
