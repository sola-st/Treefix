# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
data = dataset_ops.Dataset.from_tensors(
    [dataset_ops.Dataset.range(10) for _ in range(10)])
data = data.unbatch().flat_map(lambda x: x)
self.assertDatasetProduces(data, list(range(10)) * 10)
