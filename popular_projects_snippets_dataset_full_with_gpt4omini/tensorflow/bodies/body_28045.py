# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(
    ([0, 1, 2, 3], ['a', 'b', 'c', 'd']))
dataset = dataset.padded_batch(2)
self.assertDatasetProduces(dataset, [([0, 1], ['a', 'b']),
                                     ([2, 3], ['c', 'd'])])
