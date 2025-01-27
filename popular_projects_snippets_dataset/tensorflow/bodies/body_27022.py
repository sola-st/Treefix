# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(42)
io.save(dataset, self._test_dir, shard_func=lambda x: x % 7)
dataset2 = io.load(
    self._test_dir,
    dataset.element_spec,
    reader_func=lambda x: x.flat_map(lambda y: y))
expected = []
for i in range(7):
    expected.extend(range(i, 42, 7))
self.assertDatasetProduces(dataset2, expected)
