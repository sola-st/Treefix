# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = apply_map(dataset, lambda x: [x, constant_op.constant(37.0)])
self.assertDatasetProduces(
    dataset, expected_output=[(i, 37.0) for i in range(10)])
