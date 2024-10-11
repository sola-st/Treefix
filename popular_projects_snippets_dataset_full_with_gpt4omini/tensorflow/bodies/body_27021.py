# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(42)
io.save(dataset, self._test_dir, shard_func=lambda x: x // 21)
dataset2 = io.load(self._test_dir, dataset.element_spec)
expected = []
for i in range(21):
    expected.extend([i, i + 21])
self.assertDatasetProduces(dataset2, expected)
