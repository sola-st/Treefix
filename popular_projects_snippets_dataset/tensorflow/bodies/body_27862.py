# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(42)
dataset.save(self._test_dir, shard_func=lambda x: x // 21)
dataset2 = dataset_ops.Dataset.load(self._test_dir, dataset.element_spec)
expected = []
for i in range(21):
    expected.extend([i, i + 21])
self.assertDatasetProduces(dataset2, expected)
