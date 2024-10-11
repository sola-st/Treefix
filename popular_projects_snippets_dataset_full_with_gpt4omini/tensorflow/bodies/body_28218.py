# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = apply_map(dataset, lambda x: {"foo": x * 2, "bar": x**2})
dataset = apply_map(dataset, lambda d: d["foo"] + d["bar"])
self.assertDatasetProduces(
    dataset, expected_output=[i * 2 + i**2 for i in range(10)])
