# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
dataset = dataset_ops.Dataset.zip(
    (dataset_ops.Dataset.range(10),
     dataset_ops.Dataset.from_tensors(True).repeat(None)))
dataset = apply_filter(dataset, lambda x, y: y)
self.assertDatasetProduces(
    dataset, expected_output=[(i, True) for i in range(10)])
